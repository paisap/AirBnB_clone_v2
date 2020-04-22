#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_storage():
    """ -.... """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ display a HTML page: """
    states = storage.all(States)
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
