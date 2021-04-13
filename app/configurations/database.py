
#Importante apenas para typehint
from flask import Flask
# Importando para termos conexão com o banco de dados
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app: Flask):
    db.init_app(app)
    app.db = db
    
    from app.models.feedback import FeedbackModel