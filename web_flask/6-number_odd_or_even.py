#!/usr/bin/python3
"""
A simple Flask web application that listens on 0.0.0.0, port 5000
and displays:
- "Hello HBNB!" at the root URL
- "HBNB" at /hbnb
- "C " followed by the value of the text variable at /c/<text>
- "Python " followed by the value of the text variable.
- "n is a number" only if n is an integer at /number/<n>
- A HTML page with "Number: n" inside an H1 tag.
- A HTML page with "Number: n is even|odd" inside an H1 tag.
"""

from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Returns a string 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Returns a string 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Returns 'C ' followed by the value of the text variable"""
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """Returns 'Python ' followed by the value of the text variable"""
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n):
    """Returns 'n is a number' only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    """Renders an HTML page with 'Number: n'"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Renders an HTML page with 'Number: n is even|odd'"""
    odd_or_even = "even" if n % 2 == 0 else "odd"
    return render_template(
        '6-number_odd_or_even.html',
        n=n,
        odd_or_even=odd_or_even
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
