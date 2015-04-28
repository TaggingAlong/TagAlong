from flask import Flask

from app import app
from app.database import db_session, engine
from app.models.users import users, Users

import json

@app.route("/user/<user_name>")
@app.route("/User/<user_name>")
def get_user(user_name):
    usr = Users.query.filter_by(username=user_name).first()
    #print(usr.id_users)
    #print(usr.user_name)
    js = {
            "user_id": usr.id_users,
            "user_name": usr.username,
            "user_email": usr.email,
            "user_level": usr.level}
    return (json.dumps(js, sort_keys=True, indent=2))
