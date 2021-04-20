from flask import Flask
# Importante apenas para typehint
# Importando para termos conexão com o banco de dados
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_app(app: Flask):
    db.init_app(app)
    app.db = db

    from app.models.feedback_model import FeedbackModel
    from app.models.signup_client_model import ClientModel
    from app.models.signup_company_model import CompanyModel
    from app.models.service_resquest_catolog_model import ServiceRequestCatologModel
    from app.models.service_specific_model import ServiceSpecificModel
    from app.models.service_catolog_model import ServiceCatologModel

