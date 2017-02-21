from EVMS import app, db
from controlaccounts.form import ControlAccountForm
from controlaccounts.models import ControlAccount
from flask import render_template, redirect, url_for, request, session
from users.decorators import *
from project.models import Project
from accounttypes.models import AccountType
from spreadprofile.models import SpreadProfile

@app.route('/newcontrolaccount', methods=['POST', 'GET'])
def newcontrolaccount():
    form = ControlAccountForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print ('hey')
        #accounttype = form.accounttype.data
        project_id = form.project.get_pk(form.project.data)
        project = Project.query.filter_by(id= project_id).first()
        spread_id = form.curve.get_pk(form.curve.data)
        spread = SpreadProfile.query.filter_by(id= spread_id).first()
        accounttype_id = form.accounttype.get_pk(form.accounttype.data)
        accounttype = AccountType.query.filter_by(id= accounttype_id).first()
        parent_id = form.parent.get_pk(form.parent.data) if form.parent.data is not None else None
        parent = ControlAccount.query.filter_by(id= parent_id).first()
        print(project)
        controlaccount = ControlAccount (code= form.code.data, 
                            name= form.name.data,
                            accounttype = accounttype,
                        	budget = form.budget.data,
                        	PMB_start = form.PMB_start.data,
                        	PMB_finish = form.PMB_finish.data,
                        	PMU_start = form.PMU_start.data,
                        	PMU_finish = form.PMU_finish.data,
                        	parent = parent,
                        	curve = spread,
                        	project = project
                            )
        print (project)
        db.session.add(controlaccount)
        print (project)
        db.session.commit()
        return redirect(url_for('ca_added'))
    return render_template('controlaccounts/newaccount.html', form=form, action='new')
    
@app.route('/caadded')
def ca_added():
    return 'Control Account Added Successfully'
    
@app.route('/view_control_accounts')
@login_required
def view_control_accounts():
    accounts = ControlAccount.query.all()
    return render_template('controlaccounts/view.html', accounts=accounts)