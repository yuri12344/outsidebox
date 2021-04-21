from . import db


class ServiceSpecificModel(db.Model):
    __tablename__ = 'services_specific'
    id = db.Column(db.Integer, primary_key=True)
    name_of_service = db.Column(db.String(55), nullable=False)
    price = db.Column(db.String(20), nullable=True)
    service_description = db.Column(db.String(25), nullable=False)
    client_name = db.Column(db.String(25), nullable=False)
    id_client = db.Column(db.Integer, nullable=True)
    date_time = db.Column(db.String(25), nullable=False)
    informations = db.Column(db.String(255), nullable=False)
    feedback_url = db.Column(db.String(25))
    aproved = db.Column(db.Boolean, nullable=False)
    responsible = db.Column(db.String(25), nullable=False)
    id_company = db.Column(db.Integer, db.ForeignKey(
        'company.id'), nullable=False)
    company = db.relationship('CompanyModel', backref=db.backref(
        "services_specific_done", lazy='joined'), lazy='joined')
