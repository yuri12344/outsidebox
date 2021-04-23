from . import db
from dataclasses import dataclass


@dataclass
class ServiceCatalogModel(db.Model):
    id: int
    name_of_service: str
    price: str
    service_description: str

    __tablename__ = 'service_catalog'

    id = db.Column(db.Integer, primary_key=True)
    name_of_service = db.Column(db.String(255), nullable=False)
    price = db.Column(db.String(255), nullable=True)
    service_description = db.Column(db.String(255), nullable=False)

    id_company = db.Column(db.Integer, db.ForeignKey(
        'company.id'), nullable=False)

    service_catalog = db.relationship('ServiceRequestCatalogModel', backref=db.backref(
        "service_request_catalog_list", lazy='joined'), lazy='joined')

    company = db.relationship('CompanyModel', backref=db.backref(
        "service_catalog_list", lazy='joined'), lazy='joined')
