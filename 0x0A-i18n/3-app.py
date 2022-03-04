#!/usr/bin/env python3
"""Flask app to trasnlate i18n
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config ():
    """config the lang for the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """home page of flask app
    """
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """locate the language and timezone for the app
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
