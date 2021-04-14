from . import db


class ServiceModel(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    service_price = db.Column(db.Integer, nullable=False)
    service_description = db.Column(db.Text, nullable=False)
    date_time =db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(255)

    user_client_id = db.Column(db.Integer,db.ForeingKey('user_company.id'), nullable-False)
    user_client = db.relationship('UserClient', backref=db.backref("service_list", lazy='joined'), lazy='joined')
