#!/usr/bin/env python3
"""Creating a user auth service
"""


from flask import Flask, jsonify, redirect, request, abort, url_for
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route("/",  methods=['GET'], strict_slashes=False)
def home():
    """home route
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    "register two users"
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=["POST"])
def sessios():
    """route for creating the sessions
    """

    email = request.form.get('email')
    password = request.form.get('password')

    log = AUTH.valid_login(email, password)
    if log is False:
        abort(401)
    new_session = AUTH.create_session(email)
    resp = jsonify({"email": email, "message": "logged in"})
    resp.set_cookie("session_id", new_session)
    return resp


@app.route('/sessions', methods=["DELETE"])
def delete_session():
    """delete the session of a user
    """
    session = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(session_id=session)
    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)
    return redirect(url_for('/'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
