from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField

class RegisterForm(Form):
    firstname = StringField('First Name', [validators.Required()])
    lastname= StringField('Last Name', [validators.Required()])
    email= EmailField ('Email', [validators.Required()])
    username = StringField('Username', [validators.Required(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.Required(), 
    validators.EqualTo('confirm', message='Passwords must match'),
    validators.Length(min=4, max=80)])
    confirm = PasswordField('Confirm Password')
    
class LoginForm(Form):
    username = StringField('Username', [
            validators.Required(),
            validators.Length(min=4, max=25)
        ])
    password = PasswordField('New Password', [
            validators.Required(),
            validators.Length(min=4, max=80)
        ])

class RoleForm(Form):
    description = StringField('Role Name', [validators.Required()])
    is_read = BooleanField('Read')
    is_create = BooleanField('Create')
    is_edit = BooleanField('Edit')
    is_delete = BooleanField('Delete')