from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField, FloatField 
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
    period1 = FloatField('Period 1')
    period2 = FloatField('Period 2')
    period3 = FloatField('Period 3')
    period4 = FloatField('Period 4')
    period5 = FloatField('Period 5')
    period6 = FloatField('Period 6')
    period7 = FloatField('Period 7')
    period8 = FloatField('Period 8')
    period9 = FloatField('Period 9')
    period10 = FloatField('Period 10')
    period11 = FloatField('Period 11')
    period12 = FloatField('Period 12')
    period13 = FloatField('Period 13')
    period14 = FloatField('Period 14')
    period15 = FloatField('Period 15')
    period16 = FloatField('Period 16')
    period17 = FloatField('Period 17')
    period18 = FloatField('Period 18')
    period19 = FloatField('Period 19')
    period20 = FloatField('Period 20')
