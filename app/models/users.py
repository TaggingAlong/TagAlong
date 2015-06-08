from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

from app.models import metadata, db_session

class Users(object):
	query = db_session.query_property()
	
	def __init__(self, username=None, email=None, passwd=None):
	    self.username = username
	    self.passwd = passwd
	    self.email = email

	def __repr__(self):
	    return '<Users %r>' % (self.id_users)

users = Table('users', metadata,
	Column('id_users', Integer, primary_key=True),
	Column('username', String),
	Column('passwd', String),
	Column('email', String)
)

mapper(Users, users)
