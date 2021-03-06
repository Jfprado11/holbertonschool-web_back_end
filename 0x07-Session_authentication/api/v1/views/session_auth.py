#!/usr/bin/env python3
"""
Getting a new view to user session log in
"""

from crypt import methods
from os import getenv
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """get the session login
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if (email is None) or (email == ""):
        return jsonify({"error": "email missing"}), 400

    if (password is None) or (password == ""):
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if (len(user) == 0):
        return jsonify({"error": "no user found for this email"}), 404

    if user[0].is_valid_password(password) is False:
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user[0].id)
    out = jsonify(user[0].to_json())
    out.set_cookie(getenv("SESSION_NAME"), session_id)
    return out


@app_views.route('/auth_session/logout', methods=['DELETE'],
                 strict_slashes=False)
def session_logout():
    """deleting a session
    """
    from api.v1.app import auth
    delete_session = auth.destroy_session(request)
    if delete_session is False:
        abort(404)
    return jsonify({}), 200
