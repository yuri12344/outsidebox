from . import db
# from dataclasses import dataclass
# from sqlalchemy import Column, integer, String
# from sqlalchemy.orm import relationship


class CompanyModel(db.Model):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(25), nullable=False)
    city = db.Column(db.String(15), nullable=False)
    state = db.Column(db.String(15), nullable=False)
    cpf_cnpj = db.Column(db.String(25), nullable=False)
    schedule = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(100), nullable=False)

    # lista de feedbaks
    # feedbacks = relationship("Feedbaks", back_populates="company")
