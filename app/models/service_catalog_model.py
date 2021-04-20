from . import db


class ServiceCatalogModel(db.Model):
    __tablename__ = 'service_catalog'
    id = db.Column(db.Integer, primary_key=True)
    name_of_service = db.Column(db.String(55), nullable=False)
    price = db.Column(db.String(20), nullable=True)
    service_description = db.Column(db.String(25), nullable=False)
    id_company = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship('CompanyModel', backref=db.backref("service_catalog_list", lazy='joined'), lazy='joined')