#!/usr/bin/env python3

from flask import send_from_directory, Response

from app import app
from app.settings import settings
from app.api import *

@app.route("/")
def hello():
	return ("Hello World!")

def get_registered_routes(rules):
	routes = ""
	for url in rules:
		routes += "Route %s (%s)\n" % (url.endpoint, url.rule)
	return (routes[:-1])

@app.route("/routes/")
def registered_routes():
	if (not app.debug):
	    return ("Nope", 403)
	return Response(get_registered_routes(app.url_map._rules), mimetype="text/plain")

if (__name__ == "__main__"):
	print(app.url_map)
	#for url in app.url_map._rules:
	#    print("Route %s (%s)" % (url.endpoint, url.rule))
	#app.run()
	app.run(debug=settings["run"]["debug"])
