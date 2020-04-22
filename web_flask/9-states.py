#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.teardown_appcontext
def close_storage(self):
    """ -.... """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ ...."""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """ -... """
    states = storage.all("State")
    state_id = []
    for i in states.values():
        if id == i.id:
            state_id = i
    return render_template("9-states.html", state=state, state_id=state_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
