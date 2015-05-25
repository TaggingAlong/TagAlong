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
		data = mdi.GetData(lst)
		code = 200
	except AttributeError:
		data = {"error": "The resource was not found."}
		code = 404
	return (jsonify(data), code)

@app.route("/media")
@app.route("/Media")
def get_all_media():
	data = {}
	try:
		med = Media.query.all()
		for med_elem in med:
			tag = Tags.query.filter_by(id_media=med_elem.id_media).all()
			lst = []
			for tag_elem in tag:
				lst.append(tag_elem.tag)
			data[med_elem.id_media] = med_elem.GetData(lst)
		code = 200
	except AttributeError:
		data = {"error": "The resource was not found."}
		code = 404
	return (jsonify(data), code)
