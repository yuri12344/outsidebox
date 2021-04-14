from flask import Flask


def init_app(app: Flask):
    from .dashboard_client import bp_client
    app.register_blueprint(bp_client)

