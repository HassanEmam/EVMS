from EVMS import app, db
from costaccounts.form import CostAccountForm
from costaccounts.models import CostAccount
from controlaccounts.models import ControlAccount
from flask import render_template, redirect, url_for, request, session
#from users.models import User
from users.decorators import *

@app.route('/newfinanceaccount', methods=['POST', 'GET'])
@login_required
def newcostaccount():
    form = CostAccountForm()
    if form.validate_on_submit():
        controlaccount_id = form.controlaccount.get_pk(form.controlaccount.data)
        controlaccount = ControlAccount.query.filter_by(id= controlaccount_id).first()
        parent_id = form.parent.get_pk(form.parent.data) if form.parent.data is not None else None
        parent = CostAccount.query.filter_by(id= parent_id).first()
        costaccount = CostAccount (form.code.data, form.name.data, controlaccount, parent)
        
        db.session.add(costaccount)
        
        db.session.commit()
        return redirect(url_for('view_cost_accounts'))
    return render_template('costaccounts/newcostaccount.html', form=form, action='new')
    
@app.route('/view_cost_accounts')
@login_required
def view_cost_accounts():
    accounts = CostAccount.query.all()
    return render_template('costaccounts/view.html', accounts=accounts)
    
@app.route('/viewcostaccount/<account_id>')
@login_required
def control_cost_details(account_id):
    account = CostAccount.query.filter_by(id= int(account_id)).first()
    print (account, account_id)
    return render_template('costaccounts/details.html', account=account)
    
@app.route('/editcostaccount/<account_id>', methods=['GET', 'POST'])
def edit_cost_account(account_id):
    account = CostAccount.query.filter_by(id= int(account_id)).first()
    form = CostAccountForm(obj= account)
    if request.method == "POST" and form.validate():
        controlaccount_id = form.controlaccount.get_pk(form.controlaccount.data)
        controlaccount = ControlAccount.query.filter_by(id= controlaccount_id).first()
        parent_id = form.parent.get_pk(form.parent.data) if form.parent.data is not None else None
        parent = CostAccount.query.filter_by(id= parent_id).first()
        #account = CostAccount (form.code.data, form.name.data, controlaccount, parent)
        account.code = form.code.data
        account.name = form.name.data
        account.controlaccount_is = controlaccount_id
        account.parent_id = parent_id
        db.session.add(account)
        #print (costaccount.code)
        db.session.commit()
        return redirect(url_for('view_cost_accounts'))
    return render_template('costaccounts/newcostaccount.html', form = form, account=account, action='edit')
