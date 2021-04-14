from . import db

class FeedbackModel(db.Model):
    __tablename__ = "feedbacks"
    id = db.Column(db.Integer, primary_key=True)
    feedback = db.Column(db.Text, nullable=False)
    user_company_id = db.Column(db.Integer, db.ForeignKey('user_company.id'), nullable=False)
    user_company = db.relationship('UserCompany', backref=db.backref("feedback_list", lazy='joined'), lazy="joined")