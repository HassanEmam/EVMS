'''


'''
from EVMS import db

class CostAccount(db.Model):
	__tablename__ ="cost_accounts"
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(80), unique=True)
	name = db.Column(db.String(80))

	controlaccount_id = db.Column('ControlAccount', db.Integer, db.ForeignKey('controlaccounts.id'))
	controlaccount = db.relationship('ControlAccount', backref='control_account')
	
	parent_id = db.Column('parent_id', db.Integer, db.ForeignKey('cost_accounts.id'))
	parent = db.relationship('CostAccount', uselist=False)
	#parent_id = db.Column(db.Integer)
	
	def __init__(self, code, name, controlaccount, parent):
		self.code = code
		self.name = name
		self.parent_id = parent.id if parent is not None else None
		self.controlaccount_id = controlaccount.id
		
	def __repr__(self):
		return self.name
	
	