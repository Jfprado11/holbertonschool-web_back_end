#!/usr/bin/env python3
"""Flask app to trasnlate i18n
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)


babel = Babel(app)


class Config ():
    """config the lang for the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """finds a user by it id
    """
    key = request.args.get("login_as")
    if key is not None:
        user = users.get(int(key))
        return user
    return None


@ app.before_request
def before_request():
    """before the request made
    """
    user = get_user()
    g.user = user


@ babel.localeselector
def get_locale():
    """locate the language and timezone for the app
    """
    lang = request.args.get("locale")
    if lang is not None:
        if lang in Config.LANGUAGES:
            return lang
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@ app.route('/')
def home():
    """home page of flask app
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
