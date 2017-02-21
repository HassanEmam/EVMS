'''
This class represents the cost accounts


'''
import uuid
from app.common.database import Database
from EVMS import db

class ControlAccount(db.Model):
	__tablename__='controlaccounts'
	id = db.Column(db.Integer, primary_key =True)
	code = db.Column(db.String(80))
	name = db.Column(db.String(80))
	type = db.Column(db.String(35), unique =True)
	budget = db.Column(db.Double(80), unique= True)
	PMB_start = db.Column(db.Date)
	PMB_finish = db.Column(db.Date)
	PMU_start = db.Column(db.Date)
	PMU_finish = db.Column(db.Date)
	parent_id = db.Column(db.Integer, db.ForeignKey('controlaccounts.id'))
	
	def __init__(self, code, name, type, budget, PMB_start, PMB_finish, PMU_start, PMU_finish, parent_id, curve, project_id, _id=None):
		
		self.name = name
		self.parent_id = parent_id
		self.project_id = project_id
		self.type = type
		self.budget = budget
		self.PMB_start = PMB_start
		self.PMB_finish = PMB_finish
		self.PMU_start = PMU_start
		self.PMU_finish = PMU_finish
		self.curve = curve
		self._id = uuid.uuid4().hex if _id is None else _id
		self.code = code
	
	def json(self):
		
		return {'_id': self._id,
				'code': self.code,
				'name': self.name,
				'type': self.type,
				'budget': self.budget,
				'PMB_start': self.PMB_start,
				'PMB_finish': self.PMB_finish,
				'PMU_finish': self.PMU_finish,
				'PMU_start': self.PMU_start,
				'curve': self.curve,
				'project_id': self.project_id,
				'parent_id': self.parent_id
				}
				
	def save_to_database(self):
		pass
		#Database.insert(table= 'controlaccounts', data= self.json())
	
	@classmethod
	def find_by_id(cls, id):
		pass
		#account = Database.find_one(table= 'controlaccounts', data= {'_id': id})
		#return cls(**account)
	
	@staticmethod
	def exist(name, code):
		pass
	