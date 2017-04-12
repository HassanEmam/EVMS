'''


'''
from EVMS import db


class WBS(db.Model):
	__tablename__='wbs'
	id = db.Column(db.Integer, primary_key =True)
	code = db.Column(db.String(80))
	name = db.Column(db.String(80))
	
	parent_id = db.Column(db.Integer)
	parent = db.relationship("WBS", backref="parent")
	project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
	project = db.relationship("Project", backref="control_account")
	
	def __init__(self, code, name, parent, project):
		self.code = code
		self.name = name
		self.parent_id = parent.id if parent is not None else None
		self.project_id = project.id
		
		
	def __repr__(self):
		return self.name
		
