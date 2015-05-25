from flask import Flask, jsonify

from app import app
from app.models import db_session, engine
from app.models.users import users, Users

@app.route("/user/<user_name>")
@app.route("/User/<user_name>")
def get_user(user_name):
	try:
		usr = Users.query.filter_by(username=user_name).first()
		media = []
		data = {
			"user_id": usr.id_users,
			"user_name": usr.username,
			"user_email": usr.email,
			"user_media": media,
			"user_media_count": len(media)}
		code = 200
	except AttributeError:
		data = {"error": "The user profile doesn’t exist."}
		code = 404
	return (jsonify(data), code)

@app.route("/user/id/<int:id>")
@app.route("/User/id/<int:id>")
def get_user_id(id):
	try:
		usr = Users.query.filter_by(id_users=id).first()
		media = []
		data = {
			"user_id": usr.id_users,
			"user_name": usr.username,
			"user_email": usr.email,
			"user_media": media,
			"user_media_count": len(media)}
		code = 200	
	except AttributeError:
		data = {"error": "The user profile doesn’t exist."}
		code = 404
	return (jsonify(data), code)
