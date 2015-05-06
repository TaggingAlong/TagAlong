from flask import Flask, jsonify, Response

from app import app
from app.models import db_session, engine
from app.models.tags import tags, Tags
from app.models.media import media, Media

import json

@app.route("/tag/<path:tags>")
@app.route("/Tag/<path:tags>")
def get_tag(tags):
	data = []
	tag = db_session.query(Tags).filter(Tags.tag.in_(tags.split("/"))).all()
	for elem in tag:
		media = Media.query.filter_by(id_media=elem.id_media).first()
		tg = Tags.query.filter_by(id_media=elem.id_media).all()
		lst = []
		for ele in tg:
			lst.append(ele.tag)
		print(lst)
		data.append({
			"media_name": media.filename,
			"media_hash": media.hash,
			"media_path": "storage/%s" % (media.filename),
			"media_mime": "",
			"media_thumb": "storage/t%s" % (media.filename),
			"media_width": media.width,
			"media_height": media.height,
			"media_tags": lst
			})
	#print(data)
	resp = Response(json.dumps(data, indent=2))
	resp.mimetype = "application/json"
	return (resp)
	#return (jsonify(data))
