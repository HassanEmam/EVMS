from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from users.models import User
from wtforms.ext.sqlalchemy.fields import QuerySelectField




class ProjectSetupForm(Form):
    code = StringField('Code', [validators.Required()])
    name= StringField('Project Name', [validators.Required()])
    description = TextAreaField ('Description', [validators.Required()])
    start = DateField('Start Date', [validators.Required()])
    finish = DateField('Finish Date', [validators.Required()])
    #owner = QuerySelectField('users', query_factory= get_user)
    status = BooleanField('Active')
