#!/usr/bin/python3
"""
A simple Flask web application that listens on 0.0.0.0, port 5000
and displays:
- "Hello HBNB!" at the root URL
- "HBNB" at /hbnb
- "C " followed by the value of the text variable at /c/<text>
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Returns a string 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a string 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns 'C ' followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
