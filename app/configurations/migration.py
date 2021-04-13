#Import para typehinting
from flask import Flask
#Import para o uso da biblioteca
from flask_migrate import Migrate

def init_app(app: Flask):
    Migrate(app, app.db)


