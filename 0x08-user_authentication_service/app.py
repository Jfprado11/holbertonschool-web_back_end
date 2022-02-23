#!/usr/bin/env python3
"""Creating a user auth service
"""

from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/",  methods=['GET'], strict_slashes=False)
def home() -> None:
    """home route
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
