from EVMS import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key =True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique =True)
    username = db.Column(db.String(80), unique= True)
    password = db.Column(db.String(80))
    is_admin = db.Column(db.Boolean)
    
    
    def __init__(self, firstname, lastname, email, username, password, is_admin=False):
        self.firstname = firstname
        self.email = email
        self.lastname = lastname
        self.password = password
        self.is_admin = is_admin
        self.username = username

    def __repr__(self):
        return self.username