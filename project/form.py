from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from calendars.models import ReportingCycle
from wtforms.ext.sqlalchemy.fields import QuerySelectField




class ProjectSetupForm(Form):
    
    def get_cycles():
        return ReportingCycle.query
    
    code = StringField('Code', [validators.Required()])
    name= StringField('Project Name', [validators.Required()])
    description = TextAreaField ('Description', [validators.Required()])
    start = DateField('Start Date', [validators.Required()])
    finish = DateField('Finish Date', [validators.Required()])
    #owner = QuerySelectField('users', query_factory= get_user)
    
    cycle = QuerySelectField('Reporting Cycle', query_factory= get_cycles, allow_blank=True)
    status = BooleanField('Active')
