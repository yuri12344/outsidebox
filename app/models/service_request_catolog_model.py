from . import db


class ServiceRequestCatologModel(db.Model):
    __tablename__ = 'service_request_catolog'

    id = db.Column(db.Integer, primary_key=True)
    id_service_catolog = db.Column(db.Integer, db.ForeignKey('services_catalog.id'), nullable=False)
    client_name = db.Column(db.String(55), nullable=False)
    id_client = db.Column(db.Integer, nullable=True)
    date_time = db.Column(db.String(25), nullable=False)
    informations = db.Column(db.String(255))
    feedback_url = db.Column(db.String(55), nullable=False)
    aproved = db.Column(db.String(55), nullable=False, unique=True)
    responsible = db.Column(db.String(55), nullable=False)
    company = db.relationship('CompanyModel', backref=db.backref("services_catolog_done", lazy='joined'), lazy='joined')
