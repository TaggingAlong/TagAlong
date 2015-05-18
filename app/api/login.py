from flask import Flask, jsonify, request

from app import app, cypher
from app.models import db_session, engine
from app.models.users import users, Users

@app.route("/login", methods=['GET'])
@app.route("/Login", methods=['GET'])
def login_get():
	try:
		usr = Users.query.first()
		data = {
				"login_token": "0123456789ABCDEF",
				"login_ttl": 3600
				}
	except AttributeError:
		data = {}
	return (jsonify(data))

@app.route("/login", methods=['POST'])
@app.route("/Login", methods=['POST'])
def login_post():
	try:
		r = request.form.to_dict()
		r["user_password"] = cypher(r["user_password"])
		usr = Users.query.filter_by(username=r["user_name"], passwd=r["user_password"]).first()
		if (type(usr) == type(None)):
			raise Exception("Bad credentials.")
		data = {
				"login_token": "0123456789ABCDEF",
				"login_ttl": 3600
				}
	except AttributeError:
		data = {"error": "AttributeError"}
	except KeyError:
		data = {"error": "Missing argument."}
	except Exception as e:
		data = {"error": str(e)}
	return (jsonify(data))
