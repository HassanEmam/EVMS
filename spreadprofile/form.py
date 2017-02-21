from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from spreadprofile.models import SpreadProfile
from wtforms.ext.sqlalchemy.fields import QuerySelectField

'''
code, name, earns
'''


class SpreadForm(Form):
    code = StringField('Code', [validators.Required()])
    name= StringField('Profile Name', [validators.Required()])
    period1 = StringField('Period 1', [validators.Required(), validators.Length(max=3)])
    period2 = StringField('Period 2', [validators.Required(), validators.Length(max=3)])
    period3 = StringField('Period 3', [validators.Required(), validators.Length(max=3)])
    period4 = StringField('Period 4', [validators.Required(), validators.Length(max=3)])
    period5 = StringField('Period 5', [validators.Required(), validators.Length(max=3)])
    period6 = StringField('Period 6', [validators.Required(), validators.Length(max=3)])
    period7 = StringField('Period 7', [validators.Required(), validators.Length(max=3)])
    period8 = StringField('Period 8', [validators.Required(), validators.Length(max=3)])
    period9 = StringField('Period 9', [validators.Required(), validators.Length(max=3)])
    period10 = StringField('Period 10', [validators.Required(), validators.Length(max=3)])
    period11 = StringField('Period 11', [validators.Required(), validators.Length(max=3)])
    period12 = StringField('Period 12', [validators.Required(), validators.Length(max=3)])
    period13 = StringField('Period 13', [validators.Required(), validators.Length(max=3)])
    period14 = StringField('Period 14', [validators.Required(), validators.Length(max=3)])
    period15 = StringField('Period 15', [validators.Required(), validators.Length(max=3)])
    period16 = StringField('Period 16', [validators.Required(), validators.Length(max=3)])
    period17 = StringField('Period 17', [validators.Required(), validators.Length(max=3)])
    period18 = StringField('Period 18', [validators.Required(), validators.Length(max=3)])
    period19 = StringField('Period 19', [validators.Required(), validators.Length(max=3)])
    period20 = StringField('Period 20', [validators.Required(), validators.Length(max=3)])
