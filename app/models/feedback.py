from . import db

class FeedbackModel(db.Model):
    __tablename__ = "feedbacks"
    id = db.Column(db.Integer, primary_key=True)

