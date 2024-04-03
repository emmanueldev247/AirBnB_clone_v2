#!/usr/bin/python3
"""script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:num>", strict_slashes=False)
def number(num):
    return "{} is a number".format(num)


if __name__ == "__main__":
    app.run(debug=True)
