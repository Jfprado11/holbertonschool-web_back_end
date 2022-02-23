#!/usr/bin/env python3
"""Creating a user auth service
"""

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    """home route
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
