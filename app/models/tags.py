from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

from app.models import metadata, db_session

class Tags(object):
	query = db_session.query_property()
	
	def __init__(self, id_tags=None, id_media=None, tag=None):
			self.id_tags = id_tags
			self.id_media = id_media
			self.tag = tag			

	def __repr__(self):
			return '<Tags %r>' % (self.tag)

tags = Table('tags', metadata,
	Column('id_tags', Integer, primary_key=True),
	Column('id_media', Integer),
	Column('tag', String(255))
)

mapper(Tags, tags)
