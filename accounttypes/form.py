from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from accounttypes.models import AccountType
from wtforms.ext.sqlalchemy.fields import QuerySelectField

'''
code, name, earns
'''


class TypeForm(Form):
    code = StringField('Code', [validators.Required()])
    name= StringField('Type Name', [validators.Required()])
    
    earns = BooleanField('Earns Value')
    
  