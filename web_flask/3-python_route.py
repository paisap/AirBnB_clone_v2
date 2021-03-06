#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, request
app = Flask(__name__)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def the_python(text="is cool"):
    """ documentation """
    return "Python " + text.replace("_", " ")


@app.route('/c/<text>', strict_slashes=False)
def the_c(text):
    """ documentation"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hola"""
    return 'HBNB'


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    print("hola estoy debugeando bien pro :'")
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
