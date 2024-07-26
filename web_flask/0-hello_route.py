#!/usr/bin/python3
"""
A simple Flask web application that listens on 0.0.0.0, port 5000
and displays "Hello HBNB!" at the root URL.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Returns a string 'Hello HBNB!'"""
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
