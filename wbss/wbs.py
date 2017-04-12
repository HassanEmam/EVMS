'''
This class represents the work breakdown structure


'''
import uuid
from app.common.database import Database


class WBS(object):

	def __init__(self, code, name, parent_id, project_id, _id=None):
		self.name = name
		self.parent_id = parent_id
		self.project_id = project_id
		self._id = uuid.uuid4().hex if _id is None else _id
		self.code = code
	
	def json(self):
		return {'_id': self._id,
				'code': self.code,
				'name': self.name,
				'project_id': self.project_id,
				'parent_id': self.parent_id
				}
				
	def save_to_database(self):
		Database.insert(table= 'wbs', data= self.json())
	
	@classmethod
	def find_by_id(cls, id):
		account = Database.find_one(table= 'wbs', data= {'_id': id})
		return cls(**account)
	
	@classmethod
	def exist(name, code):
		wbs_code = Database.find_one(table= 'wbs', data= {'code': self.code})
		wbs_name = Database.find_one(table= 'wbs', data= {'code': self.code})
		if wbs_code or wbs_name:
			return True
		else:
			return False