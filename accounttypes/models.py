'''


'''
from EVMS import db
from controlaccounts.models import ControlAccount

class AccountType(db.Model):
	__tablename__='control_account_types'
	id = db.Column(db.Integer, primary_key =True)
	code = db.Column(db.String(80), unique =True)
	name = db.Column(db.String(80), unique =True)
	earns = db.Column(db.Boolean)
	

	
	def __init__(self, code, name, earns):
		
		self.name = name
		self.code = code
		self.name = name
		self.earns = earns
		
	def __repr__(self):
		return self.name