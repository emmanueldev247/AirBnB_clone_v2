#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(debug=True)
