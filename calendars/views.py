from EVMS import app, db
from calendars.form import CycleForm
from calendars.models import ReportingCycle
from flask import render_template, redirect, url_for, request, session



'''
This code controls the creation, editing, viewing and deleting of organisations
'''


@app.route('/newcycle', methods=['POST', 'GET'])
def add_cycle():
    form = CycleForm()
    
    if request.method == "POST" and form.validate():
        cycle = ReportingCycle (code= form.code.data, 
                            name= form.name.data, 
                            cycle_type= form.cycle_type.data,
                            cycle_value = form.cycle_value.data,
                            is_active= form.is_active.data)
        db.session.add(cycle)
        db.session.commit()
        return redirect(url_for('view_cycles'))
        
    return render_template('calendars/cycleform.html', form=form, action='new')


@app.route('/viewcycles')
def view_cycles():
    cycles = ReportingCycle.query.all()
    return render_template('calendars/view.html', cycles=cycles)

@app.route('/editcycle/<id>', methods=['GET', 'POST'])
def edit_cycle(id):
    cycle = ReportingCycle.query.filter_by(id= id).first()
    form = CycleForm(obj= cycle)
    
    if request.method == "POST" and form.validate():
        cycle.code = form.code.data
        cycle.is_active = form.is_active.data
        cycle.name = form.name.data
        cycle.cycle_type = form.cycle_type.data
        cycle.cycle_value = form.cycle_value.data

        db.session.add(cycle)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('view_cycles'))
    return render_template('calendars/cycleform.html', form = form, cycle=cycle, action='edit')
'''
@app.route('/deleteorganisation/<id>')
def delete_organisations(id):
    organisation = Organisation.query.filter_by(id= id).first()
    organisation.is_active = False
        
    db.session.add(organisation)
    db.session.commit()
    return redirect(url_for('view_organisations'))
    
'''