#!/usr/bin/env python3
"""setup a basic Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """config for app"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = LANGUAGES[0]
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/',)
def index():
    """index route"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """determine the best match with our supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "_main_":
    app.run(debug=True)
