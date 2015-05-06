from flask import Flask, jsonify

from app import app
from app.models import db_session, engine
from app.models.media import media, Media
from app.models.tags import tags, Tags

import json

@app.route("/media/<int:media>")
@app.route("/Media/<int:media>")
def get_media(media):
	try:
		mdi = Media.query.filter_by(id_media=media).first()
		tg = Tags.query.filter_by(id_media=media).all()
		lst = []
		for ele in tg:
			lst.append(ele.tag)

		data = {
				"media_name": mdi.filename,
				"media_hash": mdi.hash,
				"media_path": "storage/%s" % (mdi.filename),
				"media_thumb": "storage/t%s" % (mdi.filename),
				"media_mime": "",
				"media_tags": lst,
				"media_width": mdi.width,
				"media_height": mdi.height
				}
	except AttributeError:
		data = {}
	return (jsonify(data))
