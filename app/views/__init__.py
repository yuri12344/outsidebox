from flask import Flask


def init_app(app: Flask):
    from app.views.service_view import bp_service
    app.register_blueprint(bp_service)
    """
        Importamos e registramos corretamente nossa rota bp_service criada
    """
   