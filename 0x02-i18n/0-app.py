#!/usr/bin/env python3
""" Basic Flask app with a single GET route and html template """


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
