from . import db


class ServiceRequestCatalogModel(db.Model):
    __tablename__ = 'service_request_catalog'

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(55), nullable=False)
    date_time = db.Column(db.String(25), nullable=False)
    informations = db.Column(db.String(255))
    feedback_url = db.Column(db.String(55), nullable=False)
    aproved = db.Column(db.String(55), nullable=False, unique=True)
    responsible = db.Column(db.String(55), nullable=False)

    id_company = db.Column(db.Integer, db.ForeignKey(
        'company.id'), nullable=False)

    id_client = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)

    id_service_catalog = db.Column(db.Integer, db.ForeignKey(
        'service_catalog.id'), nullable=False)

    company = db.relationship('CompanyModel', backref=db.backref(
        "services_request_catalog_done", lazy='joined'), lazy='joined')
