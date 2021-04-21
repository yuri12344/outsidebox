from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class ClientModel(db.Model):
    __tablename__ = "user_client"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    adress = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    state = db.Column(db.String(15), nullable=False)


