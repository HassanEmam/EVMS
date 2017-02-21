from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField, FloatField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from accounttypes.models import AccountType
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from spreadprofile.models import SpreadProfile
from controlaccounts.models import ControlAccount
from project.models import Project


class ControlAccountForm(Form):
    
    def get_account_types():
        return AccountType.query
        
    def get_spread_profile():
        return SpreadProfile.query
        
    def get_control_accounts():
        return ControlAccount.query
        
    def get_projects():
        return Project.query.all()

    code = StringField('Code', [validators.Required()])
    name = StringField('Type Name', [validators.Required()])
    accounttype = QuerySelectField('Account Type', query_factory= get_account_types)
    curve = QuerySelectField('Spread Profile', query_factory= get_spread_profile)
    budget = FloatField('Budget', [validators.Required()])
    PMB_start = DateField('Planned Start', [validators.Required()])
    PMB_finish = DateField('Planned Finish', [validators.Required()])
    PMU_start = DateField('Anticipated Start')
    PMU_finish = DateField('Anticipated Finish')
    parent = QuerySelectField('Parent Account', query_factory= get_control_accounts, allow_blank=True)
    #parent_id = IntegerField('Parent ID')
    project = QuerySelectField('Project', query_factory= get_projects)
    
    