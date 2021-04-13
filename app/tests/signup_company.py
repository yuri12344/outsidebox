from . import db

class FeedbackModel(db.Model):
    __tablename__ = "service"
    id = db.Column(db.Integer, primary_key=True)