from . import db


class ServicesCatologModel(db.Model):
    __tablename__ = 'service_catolog'
    id = db.Column(db.Integer, primary_key=True)
    name_of_service = db.Column(db.String(55), nullable=False)
    price = db.Column(db.String(20), nullable=True)
    service_description = db.Column(db.String(25), nullable=False)
    id_company = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
    company = db.relationship('CompanyModel', backref=db.backref("service_catolog_list", lazy='joined'), lazy='joined')