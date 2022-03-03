#!/usr/bin/env python3
"""Flask app to trasnlate i18n
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)

babel = Babel(app)


class Config ():
    """config the lang for the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """locate the language and timezone for the app
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
