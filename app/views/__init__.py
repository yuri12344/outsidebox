from flask import Flask


def init_app(app: Flask):
    from .dashboard_client import bp_client
    app.register_blueprint(bp_client)

    from app.views.service_view import bp_service
    app.register_blueprint(bp_service)

    from app.views.feedback_view import bp_feedback
    app.register_blueprint(bp_feedback)

    from .client_data_views import bp_client_data
    app.register_blueprint(bp_client_data)
