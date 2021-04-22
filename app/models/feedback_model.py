from . import db
# from dataclasses import dataclass
# from sqlalchemy import Column, integer, String
# from sqlalchemy.orm import relationship


class FeedbackModel(db.Model):
    __tablename__ = "feedbacks"
    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.Text, nullable=False)
    # id_company = db.Column(db.Integer, db.ForeignKey(
    #     'company.id'), nullable=False)
    # company = db.relationship('CompanyModel', backref=db.backref(
    #     "feedback_list", lazy='joined'), lazy="joined")

    # id_company = db.Column(db.Integer, db.ForeignKey('company.id'))  # nome da tabela . nome da coluna da
    # company = db.
