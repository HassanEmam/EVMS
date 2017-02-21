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
        return redirect(url_for('ca_added'))
    return render_template('costaccounts/newcostaccount.html', form=form, action='new')
    
@app.route('/view_cost_accounts')
@login_required
def view_cost_accounts():
    accounts = CostAccount.query.all()
    return render_template('costaccounts/view.html', accounts=accounts)