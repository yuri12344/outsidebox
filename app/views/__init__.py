from flask import Flask


def init_app(app: Flask):
<<<<<<< HEAD
    from app.views.service_catalog_view import bp_service_catalog
    app.register_blueprint(bp_service_catalog)
=======
    from app.views.signup_company_view import bp_signup_comapany
    app.register_blueprint(bp_signup_comapany)

>>>>>>> af6eb7a58e63abd8172b56aabe9874463fae20b9
    # from app.views.service_view import bp_service
    # app.register_blueprint(bp_service)
    #
    # from app.views.feedback_view import bp_feedback
    # app.register_blueprint(bp_feedback)
    #
