from EVMS import app, db
from organisations.form import OrganisationForm
from organisations.models import Organisation
from flask import render_template, redirect, url_for, request, session



'''
This code controls the creation, editing, viewing and deleting of organisations
'''


@app.route('/neworganisation', methods=['POST', 'GET'])
def add_organisation():
    form = OrganisationForm()
    
    if request.method == "POST" and form.validate():
        organisation = Organisation (code= form.code.data, 
                            name= form.name.data, 
                            description= form.description.data,
                            admin = form.admin.data,
                            is_active= form.is_active.data)
        db.session.add(organisation)
        db.session.commit()
        return redirect(url_for('view_organisations'))
        
    return render_template('organisations/organisationform.html', form=form, action='new')


@app.route('/vieworganisations')
def view_organisations():
    organisations = Organisation.query.filter_by(is_active=True).all()
    return render_template('organisations/view.html', organisations=organisations)

@app.route('/editorganisation/<id>', methods=['GET', 'POST'])
def edit_organisation(id):
    organisation = Organisation.query.filter_by(id= id).first()
    form = OrganisationForm(obj= organisation)
    
    if request.method == "POST" and form.validate():
        organisation.code = form.code.data
        organisation.is_active = form.is_active.data
        organisation.name = form.name.data
        organisation.description = form.description.data
        organisation.admin = form.admin.data
        
        db.session.add(organisation)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('view_organisations'))
    return render_template('organisations/organisationform.html', form = form, organisation=organisation, action='edit')

@app.route('/deleteorganisation/<id>')
def delete_organisations(id):
    organisation = Organisation.query.filter_by(id= id).first()
    organisation.is_active = False
        
    db.session.add(organisation)
    db.session.commit()
    return redirect(url_for('view_organisations'))