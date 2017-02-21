from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from users.models import User
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from 


class CostAccountForm(Form):
    
    def get_control_account():
        return ControlAccount.query
        
    def get_cost_account():
        return CostAccount.query
    
    code = StringField('Code', [validators.Required()])
    name= StringField('Project Name', [validators.Required()])
    parent_id = QuerySelectField('cost_accounts', query_factory= get_control_account)
    control_account_id = QuerySelectField('control_account', query_factory= get_cost_account)

    
