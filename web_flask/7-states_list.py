#!/usr/bin/python3
"""A simple Flask web application that displays a list of states.

This application listens on 0.0.0.0, port 5000. It retrieves a list of all State
objects from a database using the DBStorage model in the 'models' module, and
renders an HTML page with the list.

To run the application, ensure that the following dependencies are installed:
- Flask
- models (imported from the 'models' module)

Assumptions:
- The application assumes that the database is set up correctly and contains a
  table named 'states' with columns 'id' and 'name'.

Routes:
- /states_list: HTML page with a list of all State objects in DBStorage.

Functions:
- states_list: Retrieves a list of all State objects from the database and
  renders an HTML page with the list.
- teardown_appcontext: Closes the database connection after each request.

"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage."""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_appcontext(exc):
    """Closes the database connection after each request."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
