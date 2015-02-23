from flask import Flask

from app import app
from app.database import db_session, engine
from app.models.users import users, Users

@app.route("/user/<username>")
@app.route("/User/<username>")
def get_user(username):
	con = engine.connect()
	usr = con.execute(users.select())
	#print(Users().query)
	return ("Hello World!")