from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from users.models import User
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from costaccounts.models import CostAccount
from controlaccounts.models import ControlAccount


class CostAccountForm(Form):
    
    def get_control_account():
        return ControlAccount.query
        
    def get_cost_account():
        return CostAccount.query
    
    code = StringField('Code', [validators.Required()])
    name= StringField('Account Name', [validators.Required()])
    controlaccount = QuerySelectField('Control Account', query_factory= get_control_account)
    parent = QuerySelectField('Parent Account', query_factory= get_cost_account, allow_blank=True)

    
