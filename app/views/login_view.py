from flask import Blueprint, jsonify

bp = Blueprint('/login', __name__)


@bp.route('/login', methods=["POST", "GET"])
def login():
    return "logado"
