from . import db
# from dataclasses import dataclass
# from sqlalchemy import Column, integer, String
# from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class FeedbackModel(db.Model):
    id: int
    feedback: str

    __tablename__ = "feedbacks"
    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.Text, nullable=False)
    # id_company = db.Column(db.Integer, db.ForeignKey(
    #     'company.id'), nullable=False)
    # company = db.relationship('CompanyModel', backref=db.backref(
    #     "feedback_list", lazy='joined'), lazy="joined")
    company = db.relationship('CompanyModel', backref=db.backref(
        "feedbacks_list", lazy='joined'), lazy='joined')

    # nome da tabela . nome da coluna models.DateField(_(""), auto_now=False, auto_now_add=False)
    company_id = db.Column(db.Integer, db.ForeignKey(
        'company.id', ondelete='CASCADE', onupdate="CASCADE"))

    #company = db.relationship('CompanyModel', backref="feedback_list")
