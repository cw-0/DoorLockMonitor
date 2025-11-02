from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def get_id(self):
        return int(self.user_id)

class Doors(db.Model):
    __tablename__ = "doors"
    door_id = db.Column(db.Integer, primary_key=True)
    doorname = db.Column(db.String(25), unique=True, nullable=False)
    status = db.Column(db.String(25), nullable=False)
