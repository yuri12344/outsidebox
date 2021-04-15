from . import db


class ServiceModel(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    service_price = db.Column(db.Integer, nullable=False)
    service_description = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.String(25), nullable=False)
    link = db.Column(db.String(255))
    client_name = db.Column(db.String(55), nullable=False)
    client_email = db.Column(db.String(55), nullable=False, unique=True)
    phone = db.Column(db.String(55), nullable=False)
    service_approval = db.Column(db.String(55), nullable=False)
    user_client_id = db.Column(db.Integer, db.ForeignKey('user_client.id'), nullable=False)
    user_client = db.relationship('UserClient', backref=db.backref("service_list", lazy='joined'), lazy='joined')
