from flask import Flask, jsonify

from app import app
from app.models import db_session, engine
from app.models.media import media, Media

import json

@app.route("/media/<int:media>")
@app.route("/Media/<int:media>")
def get_media(media):
	try:
		#mdi = Media.query.filter_by(media=id_media).first()
		media = []
		data = {}
	except AttributeError:
		data = {}
	return (jsonify(data))
