#!/usr/bin/env python3
""" Basic Flask app """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)

# Instantiate the Babel object
babel = Babel(app)

# Create a Config class with available languages
class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)  # Use Config as the app configuration

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
