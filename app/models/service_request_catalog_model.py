from . import db
from dataclasses import dataclass


@dataclass
class ServiceRequestCatalogModel(db.Model):
    id: int
    client_name: str
    date_time: str
    informations: str
    feedback_url: str
    aproved: str
    responsible: str

    __tablename__ = 'service_request_catalog'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(55), nullable=False)
    date_time = db.Column(db.String(100), nullable=False)
    informations = db.Column(db.String(255))
    feedback_url = db.Column(db.String(255), nullable=True)
    aproved = db.Column(db.String(55), nullable=False)
    responsible = db.Column(db.String(55), nullable=False)
    hash_to_feedback = db.Column(db.String(255), nullable=True, unique=True)

    id_company = db.Column(db.Integer, db.ForeignKey(
        'company.id'), nullable=False)

    id_client = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=True)

    id_service_catalog = db.Column(db.Integer, db.ForeignKey(
        'service_catalog.id'), nullable=False)

    company = db.relationship('CompanyModel', backref=db.backref(
        "services_request_catalog_done", lazy='joined'), lazy='joined')
