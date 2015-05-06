from flask import Flask, jsonify

from app import app
from app.models import db_session, engine
from app.models.users import users, Users

import json

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
	except AttributeError:
		data = {}
	return (jsonify(data))
