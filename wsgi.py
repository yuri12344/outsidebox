from app import create_app
from whitenoise import WhiteNoise

if __name__ == 'main':
    application = create_app()
    application.run("0.0.0.0")
