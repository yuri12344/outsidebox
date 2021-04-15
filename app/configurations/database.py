from flask import Flask
# Importante apenas para typehint
# Importando para termos conexão com o banco de dados
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.feedback_model import FeedbackModel
    from app.models.user_client_model import UserClient
    from app.models.user_company_model import UserCompany
    from app.models.service_model import ServiceModel
