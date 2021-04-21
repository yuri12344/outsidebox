from flask import Flask


def init_app(app: Flask):

    # from app.views.feedback_view import bp_feedback
    # app.register_blueprint(bp_feedback)

    from app.views.signup_client_view import bp_client
    app.register_blueprint(bp_client)

    from app.views.service_catalog_view import bp_service_catalog
    app.register_blueprint(bp_service_catalog)
    from app.views.signup_company_view import bp_signup_company
    app.register_blueprint(bp_signup_company)
    from app.views.service_specific_view import bp_service_specific
    app.register_blueprint(bp_service_specific)

    # from app.views.login_view import bp_login, bp_protected, bp_unprotected
    # app.register_blueprint(bp_login)

    # app.register_blueprint(bp_protected)
    # app.register_blueprint(bp_unprotected)

    # from app.views.service_view import bp_service
    # app.register_blueprint(bp_service)
    # from app.views.feedback_view import bp_feedback
    # app.register_blueprint(bp_feedback)
