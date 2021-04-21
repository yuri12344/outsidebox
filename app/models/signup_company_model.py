from . import db
from werkzeug.security import generate_password_hash, check_password_hash


class CompanyModel(db.Model):
    __tablename__ = 'user_company'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    adress = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    state = db.Column(db.String(15), nullable=False)
    cpf_cnpj = db.Column(db.String(25), nullable=False)
    schedule = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=False)
