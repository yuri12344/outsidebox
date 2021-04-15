from flask import Flask


def init_app(app: Flask):
    from app.views.service_view import bp_service
    app.register_blueprint(bp_service)

    from app.views.feedback_view import bp_feedback
    app.register_blueprint(bp_feedback)
