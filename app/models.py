from time import time
from datetime import date
from . import db


def get_new_id():
	new_id = long(time())
	return new_id
	

def timeinfo():
    d = date.today();
    return "{0:%A}, {0:%B} {0:%d}, {0:%y}".format(d)



class UserProfile(db.Model):
    __tablename__ = 'UserProfile'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    gender= db.Column(db.String(10))
    created_on = db.Column(db.String(30))
    bio = db.Column(db.String(250))
    photo=db.Column(db.String(80))
    location=db.Column(db.String(80))
    email=db.Column(db.String(80))
    

    def __init__(self,first_name,last_name,created_on,bio,photo,location,email):
        self.id=get_new_id()
        self.first_name=first_name
        self.last_name=last_name
        self.created_on=timeinfo()
        self.bio=bio
        self.photo=photo
        self.location=location
        self.email=email
        

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
