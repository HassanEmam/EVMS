'''
Calendar class maintains project calendar
It has properties as 
start date, 
reporting cycle type i.e. days, weeks, months
reporting cycle value number of periods for reports i.e. 1 month, 4 weeks, 30 days, etc.


'''
from EVMS import db

class ReportingCycle(db.Model):
	__tablename__ = 'reportingcycles'
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(80), unique=True)
	name = db.Column(db.String(80))
	cycle_type = db.Column(db.Text)
	cycle_value = db.Column(db.Integer)
	#project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
	#project = db.relationship('Project', backref='ReportingCalendar')
	is_active = db.Column(db.Boolean)
	
	def __init__(self, code, name, cycle_type, cycle_value, is_active = True):
		self.code = code
		self.name = name
		self.cycle_type = cycle_type
		self.cycle_value = cycle_value
		#self.project_id = project.id
		self.is_active = is_active

	def __repr__(self):
		return self.name