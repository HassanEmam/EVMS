'''


'''
from EVMS import db

class Organisation(db.Model):
	__tablename__ ="organisations"
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(80), unique=True)
	name = db.Column(db.String(80))
	description = db.Column(db.Text)
	admin_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	admin = db.relationship('User', backref='organisations')
	is_active = db.Column(db.Boolean)

	def __init__(self, code, name, description, admin, is_active=True):
		self.code = code
		self.name = name
		self.description = description
		self.admin_id = admin.id
		self.is_active = is_active
		
	def __repr__(self):
		return self.name
	
	