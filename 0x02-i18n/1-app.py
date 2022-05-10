#!/usr/bin/env python3
"""First you will setup a basic Flask app in 0-app.py.
Create a single / route and an index.html template that
simply outputs “Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>)."""
from flask import render_template, Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    This is the configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route('/', strict_slashes=False)
def index():
    """
    This is the main page of the flask application.
    Returns:
        str: The rendered template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
