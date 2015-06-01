from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper

from app.models import metadata, db_session

class Media(object):
	query = db_session.query_property()
	
	def __init__(self, id_media=None, id_users=None, filename=None, width=None, height=None, size=None, mimetype=None, hash=None):
			self.id_media = id_media
			self.id_users = id_users
			self.filename = filename
			self.width = width
			self.height = height
			self.size = size
			self.mimetype = mimetype
			self.hash = hash

	def __repr__(self):
			return '<Media %r>' % (self.id_media)

	def GetData(self, tags):
		data = {
				"media_id": self.id_media,
				"media_name": self.filename,
				"media_hash": self.hash,
				"media_path": "storage/%s" % (self.filename),
				"media_thumb": "storage/t%s" % (self.filename),
				"media_mime": self.mimetype,
				"media_tags": tags,
				"media_width": self.width,
				"media_height": self.height
				}
		return (data)

media = Table('media', metadata,
	Column('id_media', Integer, primary_key=True),
	Column('id_users', Integer),
	Column('filename', String(255)),
	Column('width', Integer),
	Column('height', Integer),
	Column('size', Integer),
	Column('mimetype', String),
	Column('hash', String(255))
)

mapper(Media, media)
