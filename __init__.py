from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate


app = Flask(__name__)
app.config.from_object('settings')
db = SQLAlchemy(app)

#Migration
migrate= Migrate(app, db)
#from app import views
from users import views
from project import views
from accounttypes import views
from spreadprofile import views
from controlaccounts import views
from costaccounts import views
from organisations import views
from calendars import views

