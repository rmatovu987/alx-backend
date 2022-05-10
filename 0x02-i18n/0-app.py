#!/usr/bin/env python3
"""First you will setup a basic Flask app in 0-app.py.
Create a single / route and an index.html template that
simply outputs “Welcome to Holberton” as page title (<title>)
and “Hello world” as header (<h1>)."""
from flask import render_template, Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    This is the main page of the flask application.
    Returns:
        str: The rendered template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
