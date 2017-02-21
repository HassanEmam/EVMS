'''


'''
from EVMS import db

class SpreadProfile(db.Model):
	__tablename__='spread_profile'
	id = db.Column(db.Integer, primary_key =True)
	code = db.Column(db.String(80), unique =True)
	name = db.Column(db.String(80), unique =True)
	period1 = db.Column(db.String(3))
	period2 = db.Column(db.String(3))
	period3 = db.Column(db.String(3))
	period4 = db.Column(db.String(3))
	period5 = db.Column(db.String(3))
	period6 = db.Column(db.String(3))
	period7 = db.Column(db.String(3))
	period8 = db.Column(db.String(3))
	period9 = db.Column(db.String(3))
	period10 = db.Column(db.String(3))
	period11 = db.Column(db.String(3))
	period12 = db.Column(db.String(3))
	period13 = db.Column(db.String(3))
	period14 = db.Column(db.String(3))
	period15 = db.Column(db.String(3))
	period16 = db.Column(db.String(3))
	period17 = db.Column(db.String(3))
	period18 = db.Column(db.String(3))
	period19 = db.Column(db.String(3))
	period20 = db.Column(db.String(3))
	
	def __init__(self, code, name, period1, period2, period3, period4, period5, period6, period7,
				period8, period9, period10, period11, period12, period13, period14, period15,
				period16, period17, period18, period19, period20):
		
		self.name = name
		self.code = code
		self.name = name
		self.period1 = period1
		self.period2 = period2
		self.period3 = period3
		self.period4 = period4
		self.period5 = period5
		self.period6 = period6
		self.period7 = period7
		self.period8 = period8
		self.period9 = period9
		self.period10 = period10
		self.period11 = period11
		self.period12 = period12
		self.period13 = period13
		self.period14 = period14
		self.period15 = period15
		self.period16 = period16
		self.period17 = period17
		self.period18 = period18
		self.period19 = period19
		self.period20 = period20
		
	def __repr__(self):
		return self.name