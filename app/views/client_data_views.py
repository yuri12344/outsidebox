from flask import Blueprint, request, current_app


bp_client_data=Blueprint('client_data', __name__)

@bp_client_data.route('/client_data/<id>',methods=["GET"])
def client_data(id):
    session = current_app.db.session
    data = request.get_json()
    jack = session.query(User).get(5)
    return "User %s" % id


