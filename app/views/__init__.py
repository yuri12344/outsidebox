from flask import Flask


def init_app(app: Flask):
    from app.views.service_catalog_view import bp_service_catalog
    app.register_blueprint(bp_service_catalog)
    from app.views.signup_company_view import bp_signup_comapany
    app.register_blueprint(bp_signup_comapany)

    # from app.views.service_view import bp_service
    # app.register_blueprint(bp_service)
    # from app.views.feedback_view import bp_feedback
    # app.register_blueprint(bp_feedback)
