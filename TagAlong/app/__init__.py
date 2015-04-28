import os, importlib

from flask import Flask, send_from_directory

from app.api import api_blueprint

from app.models import db_session, engine

app = Flask(__name__)
app.root_path = os.path.abspath(os.path.dirname(app.root_path))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/storage/<string:filename>')
def serve_media(filename):
    print(filename)
    return (send_from_directory("storage", filename))

def is_validroute(route):
    return (os.path.isfile("./app/api/%s.py" % route) and route != "__init__")

for route in os.listdir("./app/api/"):
    route = route.replace(".py", "")
    if (is_validroute(route)):
    	importlib.import_module("app.api.%s" % route)

app.register_blueprint(api_blueprint)