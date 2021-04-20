from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class ClientModel(db.Model):
    __tablename__ = "user_client"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password_hash = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    adress = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    state = db.Column(db.String(15), nullable=False)

    @property
    def password(self):
        raise TypeError('A senha não pode ser acessada')

    @password.setter
    def password(self, new_password):
        new_password_hash = generate_password_hash(new_password)
        self.password_hash = new_password_hash

    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
