from . import db

class FeedbackModel(db.Model):
    __tablename__ = "register_client"
    id = db.Column(db.Integer, primary_key=True)
