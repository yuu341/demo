from database import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key= True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=True)
    