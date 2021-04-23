from dataclasses import dataclass
from . import db


@dataclass
class ServiceSpecificModel(db.Model):
    id: int
    name_of_service: str
    price: str
    service_description: str
    client_name: str
    id_client: str
    date_time: str
    informations: str
    feedback_url: str
    aproved: str
    responsible: str

    __tablename__ = 'services_specific'
    id = db.Column(db.Integer, primary_key=True)
    name_of_service = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=True)
    service_description = db.Column(db.String(255), nullable=False)
    client_name = db.Column(db.String(255), nullable=False)
    id_client = db.Column(db.String, nullable=True)
    date_time = db.Column(db.String(255), nullable=False)
    informations = db.Column(db.String(255), nullable=False)
    feedback_url = db.Column(db.String(255), nullable=True)
    aproved = db.Column(db.String(255), nullable=False)
    responsible = db.Column(db.String(255), nullable=False)
    id_company = db.Column(db.Integer, db.ForeignKey(
        'company.id'), nullable=False)
    company = db.relationship('CompanyModel', backref=db.backref(
        "services_specific_done", lazy='joined'), lazy='joined')
