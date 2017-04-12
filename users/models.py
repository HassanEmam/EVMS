from EVMS import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key =True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique =True)
    username = db.Column(db.String(80), unique= True)
    password = db.Column(db.String(80))
    organisation_id = db.Column('Organisation', db.Integer, db.ForeignKey('organisations.id'), nullable=True)
    organisation = db.relationship('Organisation', backref='users')
    is_admin = db.Column(db.Boolean)
    
    def __init__(self, firstname, lastname, email, username, password,organisation, is_admin=False):
        self.firstname = firstname
        self.email = email
        self.lastname = lastname
        self.password = password
        self.is_admin = is_admin
        self.username = username
        if organisation is not None:
            organisation_id = organisation.id
        else:
            organisation_id = None

    def __repr__(self):
        return self.username

       
class Role(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    description = db.Column(db.String(80))
    is_read = db.Column(db.Boolean)
    is_create = db.Column(db.Boolean)
    is_edit = db.Column(db.Boolean)
    is_delete = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)
    
    def __init__(self, description, is_read, is_create, is_edit, is_delete, is_active=True):
        self.description = description
        self.is_create = is_create
        self.is_delete = is_delete
        self.is_edit = is_edit
        self.is_read = is_read
        self.is_active = is_active
        
    def _repr__(self):
        return self.description