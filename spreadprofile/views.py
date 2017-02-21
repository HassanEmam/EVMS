from EVMS import app, db
from spreadprofile.form import SpreadForm
from flask import render_template, redirect, url_for, request, session
from spreadprofile.models import SpreadProfile
from users.decorators import *

@app.route('/newspread', methods=['POST', 'GET'])
def newspread():
    form = SpreadForm()
    
    if request.method == "POST" and form.validate():

        spread_data = SpreadProfile (code= form.code.data, 
                            name= form.name.data, 
                            period1 = form.period1.data,
                    		period2 = form.period2.data,
                    		period3 = form.period3.data,
                    		period4 = form.period4.data,
                    		period5 = form.period5.data,
                    		period6 = form.period6.data,
                    		period7 = form.period7.data,
                    		period8 = form.period8.data,
                    		period9 = form.period9.data,
                    		period10 = form.period10.data,
                    		period11 = form.period11.data,
                    		period12 = form.period12.data,
                    		period13 = form.period13.data,
                    		period14 = form.period14.data,
                    		period15 = form.period15.data,
                    		period16 = form.period16.data,
                    		period17 = form.period17.data,
                    		period18 = form.period18.data,
                    		period19 = form.period19.data,
                    		period20 = form.period20.data)
        print (spread_data.name)
        db.session.add(spread_data)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('spread_added'))
    return render_template('spreadprofile/newspreadprofile.html', form=form, action='new')
    
@app.route('/spread_added')
def spread_added():
    return 'Spred Profile added successfully'
    
@app.route('/editspread/<spread_id>', methods=['POST', 'GET'])
@login_required
def edit_spread(spread_id):
    spread = SpreadProfile.query.filter_by(id= spread_id).first()
    form = SpreadForm(obj= spread)
    if request.method == "POST" and form.validate():

        spread_data = SpreadProfile (code= form.code.data, 
                            name= form.name.data, 
                            period1 = form.period1.data,
                    		period2 = form.period2.data,
                    		period3 = form.period3.data,
                    		period4 = form.period4.data,
                    		period5 = form.period5.data,
                    		period6 = form.period6.data,
                    		period7 = form.period7.data,
                    		period8 = form.period8.data,
                    		period9 = form.period9.data,
                    		period10 = form.period10.data,
                    		period11 = form.period11.data,
                    		period12 = form.period12.data,
                    		period13 = form.period13.data,
                    		period14 = form.period14.data,
                    		period15 = form.period15.data,
                    		period16 = form.period16.data,
                    		period17 = form.period17.data,
                    		period18 = form.period18.data,
                    		period19 = form.period19.data,
                    		period20 = form.period20.data)
        
        db.session.commit()
        return redirect(url_for('spread_added'))
    return render_template('spreadprofile/newspreadprofile.html', form=form, spread= spread, action='edit')
    
@app.route('/viewspreadprofiles')
def view_spread_profiles():
    profiles = SpreadProfile.query.all()
    return render_template('spreadprofile/listspreadprofiles.html', profiles= profiles)