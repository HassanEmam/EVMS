'''


'''
from EVMS import db
#from accounttypes.models import AccountType
#from project.models import Project

class ControlAccount(db.Model):
	__tablename__='controlaccounts'
	id = db.Column(db.Integer, primary_key =True)
	code = db.Column(db.String(80))
	name = db.Column(db.String(80))
	budget = db.Column(db.Float)
	PMB_start = db.Column(db.Date)
	PMB_finish = db.Column(db.Date)
	PMU_start = db.Column(db.Date)
	PMU_finish = db.Column(db.Date)
	parent_id = db.Column(db.Integer, nullable= True)
	
	accounttype_id = db.Column('AccountType', db.Integer, db.ForeignKey('control_account_types.id'))
	accounttype = db.relationship('AccountType', backref='control_account')
	curve_id = db.Column(db.Integer, db.ForeignKey('spread_profile.id'))
	curve = db.relationship("SpreadProfile", backref="control_account")
	project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
	project = db.relationship("Project", backref="control_account")
	
	def __init__(self, code, name, accounttype, budget, PMB_start, PMB_finish, PMU_start, PMU_finish, parent, curve, project):
		self.code = code
		self.name = name
		self.parent_id = parent.id if parent is not None else None
		self.accounttype_id = accounttype.id
		self.budget = budget
		self.PMB_start = PMB_start
		self.PMB_finish = PMB_finish
		self.PMU_start = PMU_start
		self.PMU_finish = PMU_finish
		if curve:
			self.curve_id = curve.id
		else:
			self.curve_id = None
		self.project = project
		self.project_id = project.id
		
		
	def __repr__(self):
		return self.name
		
