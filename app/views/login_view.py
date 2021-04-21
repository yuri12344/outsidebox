from flask import Blueprint, json, jsonify, request, make_response, current_app
import jwt
import datetime
from functools import wraps


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, 'chavesecreta', algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(*args, **kwargs)

    return decorated


bp_unprotected = Blueprint('/unprotected', __name__,
                           url_prefix='/unprotected')
bp_protected = Blueprint('/protected', __name__, url_prefix='/protected')
bp_login = Blueprint('/login', __name__, url_prefix='/login')


@bp_login.route('/')
def login():
    auth = request.authorization

    if auth and auth.password == 'secret':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow(
        ) + datetime.timedelta(minutes=10)}, "chavesecreta", algorithm="HS256")

        return jsonify({'token': token})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


@bp_unprotected.route('/')
def unprotected():
    return jsonify({'message': 'Anyone can view this!'})


@bp_protected.route('/')
@token_required
def protected():
    return jsonify({'message': 'This is only available for people with valid tokens.'})
