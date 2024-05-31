#!/usr/bin/env python3
"""necessary imports"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """class config documentation"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """The get locale method"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", strict_slashes=False)
def index():
    """index page render"""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
