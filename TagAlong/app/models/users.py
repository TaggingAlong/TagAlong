from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

from app.models import metadata, db_session

class Users(object):
	query = db_session.query_property()
	
	def __init__(self, id_user=None, username=None, email=None, passwd=None, level=None):
		self.user_id = id_user
		self.user_name = username
		self.user_email = email
		self.user_level = level
		self.user_media = []
		self.user_media_count = len(self.user_media)

	def __repr__(self):
		return '<Users %r>' % (self.name)

users = Table('users', metadata,
	Column('id_user', Integer, primary_key=True),
	Column('username', String(255)),
	Column('passwd', String(255)),
	Column('level', Integer)
)

mapper(Users, users)