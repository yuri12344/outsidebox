from flask import Flask


def init_app(app: Flask):
    # Rota 01 SIGNUP COMPANY
    from app.views.signup_company_view import bp_signup_company
    app.register_blueprint(bp_signup_company)

    # Rota 02 SERVICES CATALOG
    from app.views.service_catalog_view import bp_service_catalog
    app.register_blueprint(bp_service_catalog)

    # Rota 03 SERVICE REQUEST FROM CATALOG
    from app.views.service_request_catalog_model import bp_catalog_service_request
    app.register_blueprint(bp_catalog_service_request)

    # Rota 04 SPECIFIC SERVICE REQUEST
    from app.views.service_specific_view import bp_services_specific
    app.register_blueprint(bp_services_specific)

    # Rota 05 GET SERVICES
    from app.views.get_services_view import bp_get_services
    app.register_blueprint(bp_get_services)

    # Rota 06 UPDATE SERVICE
    from app.views.update_service import bp_update_service
    app.register_blueprint(bp_update_service)

    # Rota 07 FEEDBACK
    #from app.views.feedback_view import bp_feedback
    # app.register_blueprint(bp_feedback)

    # Rota 08 DASHBOARD COMPANY
    from app.views.dashboard_company_view import dashboard_company
    app.register_blueprint(dashboard_company)

    # Rota 09 COMPANYS
    from app.views.companys_view import bp_companys
    app.register_blueprint(bp_companys)

    # Rota 10 SIGNUP CLIENT
    from app.views.signup_client_view import bp_client
    app.register_blueprint(bp_client)

    # Rota 11 LOGIN
    # from app.views.login_view import bp_login
    # app.register_blueprint(bp_login)

    # Rota 12 CLIENT PROFILE
    from app.views.profile_client_view import bp_client_profile
    app.register_blueprint(bp_client_profile)
