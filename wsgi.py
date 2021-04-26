from app import create_app
from whitenoise import WhiteNoise

application = create_app()
if __name__ == 'main':
    application.run("0.0.0.0")
