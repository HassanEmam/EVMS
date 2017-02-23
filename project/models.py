'''


'''
from EVMS import db
from controlaccounts.models import ControlAccount

class Project(db.Model):
	__tablename__ ="projects"
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(80), unique=True)
	name = db.Column(db.String(80))
	owner = db.Column(db.Integer, db.ForeignKey('users.id'))
	description = db.Column(db.Text)
	start = db.Column(db.DateTime)
	finish = db.Column(db.DateTime)
	status = db.Column(db.Boolean)

	def __init__(self, code, name, description, owner, start, finish, status):
		self.code = code
		self.name = name
		self.owner = owner
		self.description = description
		self.start = start
		self.finish = finish
		self.status = status
		
	def __repr__(self):
		return self.name
	
	