from flask import Flask

from .views.login import bp as bp_login

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp_login)
    return app