from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from users.models import User

class OrganisationForm(Form):
    
    def get_users():
        return User.query
    
    code = StringField('Code', [validators.Required()])
    name= StringField('Project Name', [validators.Required()])
    description = TextAreaField ('Description', [validators.Required()])
    #admin = QuerySelectField('Super User', query_factory= get_users, allow_blank=True)
    is_active = BooleanField('Active')
