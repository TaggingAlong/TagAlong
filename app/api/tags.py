from flask import Flask, jsonify

from app import app
from app.models import db_session, engine
from app.models.tags import tags, Tags

import json

@app.route("/tag/<path:tags>")
@app.route("/Tag/<path:tags>")
def get_tag(tags):
	try:
		#usr = Tags.query.filter_by(tagname=user_name).first()
		media = []
		data = {}
	except AttributeError:
		data = {}
	return (jsonify(data))
