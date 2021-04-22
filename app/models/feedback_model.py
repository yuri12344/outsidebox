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

    company_id = db.Column(db.Integer, db.ForeignKey('company.id',ondelete='CASCADE',onupdate="CASCADE"))  # nome da tabela . nome da coluna models.DateField(_(""), auto_now=False, auto_now_add=False)
   
    company= db.relationship('CompanyModel', backref="feedback_list")