from flask import Flask, jsonify

from app import app
from app.models import db_session, engine
from app.models.tags import tags, Tags
from app.models.media import media, Media

@app.route("/tag/<path:tags>")
@app.route("/Tag/<path:tags>")
def get_tag(tags):
	data = {}
	tag = db_session.query(Tags).filter(Tags.tag.in_(tags.lower().split("/"))).all()
	for elem in tag:
		media = Media.query.filter_by(id_media=elem.id_media).first()
		if (media.id_media not in data):
			tg = Tags.query.filter_by(id_media=elem.id_media).all()
			lst = []
			for ele in tg:
				lst.append(ele.tag)
			data[media.id_media] = media.GetData(lst)
	code = 200
	return (jsonify(data), code)
