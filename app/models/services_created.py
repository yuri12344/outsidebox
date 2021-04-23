from . import db
from dataclasses import dataclass


@dataclass
class ServicesCreated(db.Model):
    id: str

    __tablename__ = 'services_created'
    id = db.Column(db.Integer, primary_key=True)
    id_company = db.Column(db.Integer, db.ForeignKey(
        'company.id'), nullable=False)
    from_ = db.Column(db.String(255), nullable=False)
    id_service_create_catalog = db.Column(db.Integer, db.ForeignKey(
        'service_request_catalog.id'), nullable=True)

    id_service_create_specific = db.Column(db.Integer, db.ForeignKey(
        'services_specific.id'), nullable=True)
