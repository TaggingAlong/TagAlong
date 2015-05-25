from flask import Flask, jsonify

from app import app
from app.models import db_session, engine
from app.models.media import media, Media
from app.models.tags import tags, Tags

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

@app.route("/media")
@app.route("/Media")
def get_all_media():
	data = {}
	try:
		mdi = Media.query.all()
		print(mdi)
		for elem in mdi:
			tg = Tags.query.filter_by(id_media=elem.id_media).all()
			lst = []
			for ele in tg:
				lst.append(ele.tag)
			data[elem.id_media] = {
					"media_name": elem.filename,
					"media_hash": elem.hash,
					"media_path": "storage/%s" % (elem.filename),
					"media_thumb": "storage/t%s" % (elem.filename),
					"media_mime": "",
					"media_tags": lst,
					"media_width": elem.width,
					"media_height": elem.height
					}
	except AttributeError:
		data = {}
	return (jsonify(data))
