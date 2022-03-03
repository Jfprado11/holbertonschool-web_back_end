#!/usr/bin/env python3
"""Flask app to trasnlate i18n
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """home page of flask app
    """
    return render_template("0-index.html")