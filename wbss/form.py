from flask_wtf import Form
from wtforms import validators, StringField, PasswordField, TextAreaField, BooleanField, FloatField, IntegerField
from wtforms.fields.html5 import DateField
from wtforms.fields.html5 import EmailField
from wbss.models import WBS
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from spreadprofile.models import SpreadProfile
from controlaccounts.models import ControlAccount
from project.models import Project


class WBSForm(Form):
    
    def get_wbs():
        return WBS.query   

    code = StringField('Code', [validators.Required()])
    name = StringField('Type Name', [validators.Required()])
    
    parent = QuerySelectField('Parent WBS', query_factory= get_wbs, allow_blank=True)
    #parent_id = IntegerField('Parent ID')
    #project = QuerySelectField('Project', query_factory= get_projects)
    
    