#!/usr/bin/python3
"""Flask script which displays route/ “Hello HBNB!” """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Function to define index"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def index_hbnb():
    """Funtion to define index/hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """Function to define /C/txt"""
    return 'C ' + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """display only if n is number"""
    return '{n} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def title_number(n):
    """display HTML page if n is a number"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def render_html_variables(n):
    """renders html page with variables"""
    if n % 2 == 0:
        is_odd_or_even = "even"
    else:
        is_odd_or_even = "odd"

    return render_template("6-number_odd_or_even.html", n=n, e=is_odd_or_even)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
