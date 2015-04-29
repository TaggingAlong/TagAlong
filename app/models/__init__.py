from app.settings import settings

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine('sqlite:///./test.db', convert_unicode=True)
engine = create_engine("%s://%s:%s@%s/%s" % (settings["db"]["connector"],
	settings["db"]["user"],
	settings["db"]["password"],
	settings["db"]["host"],
	settings["db"]["db"]),
	convert_unicode=True)
metadata = MetaData()
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

def init_db():
	metadata.create_all(bind=engine)
