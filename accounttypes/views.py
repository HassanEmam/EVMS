from EVMS import app, db
from accounttypes.form import TypeForm
from flask import render_template, redirect, url_for, request, session
from accounttypes.models import AccountType
from users.decorators import *

@app.route('/newtype', methods=['POST', 'GET'])
@login_required
def new_type():
    form = TypeForm()
    
    if request.method == "POST" and form.validate():

        account_type = AccountType (code= form.code.data, 
                            name= form.name.data, 
                            earns= form.earns.data)
        db.session.add(account_type)
        db.session.flush()
        db.session.commit()
        return redirect(url_for('type_added'))
    return render_template('accounttypes/newtype.html', form=form, action='new')
    
@app.route('/viewtypes')
def type_added():
    types_list = AccountType.query.all()
    return render_template('accounttypes/listtypes.html', types_list= types_list)
    
@app.route('/edittype/<type_id>', methods=['POST', 'GET'])
@login_required
def edit_type(type_id):
    
    accounttype = AccountType.query.filter_by(id= type_id).first()
    form = TypeForm(obj= accounttype)
    if request.method == "POST" and form.validate():

        account_type = AccountType (code= form.code.data, 
                            name= form.name.data, 
                            earns= form.earns.data)
        
        db.session.commit()
        return redirect(url_for('type_added'))
    return render_template('accounttypes/newtype.html', form=form, accounttype= accounttype, action='edit')