from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

from app.models import metadata, db_session

class Users(object):
	query = db_session.query_property()
	
	def __init__(self, id_users=None, username=None, email=None, passwd=None):
	    self.id_users = id_users
	    self.username = username
	    self.passwd = passwd
	    self.email = email

	def __repr__(self):
	    return '<Users %r>' % (self.id_users)

users = Table('users', metadata,
	Column('id_users', Integer, primary_key=True),
	Column('username', String(255)),
	Column('passwd', String(255)),
	Column('email', String(255))
)

mapper(Users, users)
