from . import db


class CompanyModel(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(20), nullable=False)
    cpf_cnpj = db.Column(db.String(20), nullable=False)
    schedule = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)
