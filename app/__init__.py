from flask import Flask
from os import getenv
from dotenv import load_dotenv
from app.configurations import database, migration
from app import views
import ipdb
load_dotenv()


def create_app():
    app = Flask(__name__)
    global user_logged
    user_logged = [
        {"secret_key": "chavesecreta"}, {"token": "vazio"}, {"user": "precisa fazer o login"}]

    # Aqui nós passamos o "SQLALCHEMY_DATABASE_URI" que foi feito lá no .env
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URL')[:8] + "ql" + getenv('DATABASE_URL')[8:]
    
    # Aqui nós passamos False para evitar mensagens de avisos no terminal
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Setamos como False para o Flask não organzizar nossas keys por ordem alfabetica
    app.config["JSON_SORT_KEYS"] = False

    app.config['SECRET_KEY'] = getenv('SECRET_KEY')

    # Inicializamos as configurações do nosso db e da nossa migration, que agora estão para o uso
    database.init_app(app)
    migration.init_app(app)
    views.init_app(app)

    """
        Chamamos o init das nossas views para que a nossa rotas sejam inicializadas corretamente
    """

    return app
