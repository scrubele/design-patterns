from flask import app
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import current_app

import urllib
params = urllib.parse.quote_plus("DRIVER={SQL Server};SERVER=DESKTOP-DDAN4MP;DATABASE=spotify_db;PWD=qwer1234****")
SQLALCHEMY_DATABASE_URI = "mssql+pyodbc:///?odbc_connect=%s" % params

engine = create_engine(SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from app.DAL.entities import Basic_user, Song, Basic_user_song, Session
    from app.DAL.models import BasicUserModel
    Base.metadata.create_all(bind=engine)
    column_name = db_session.query(Base.metadata.tables['basic_user']).column_descriptions[0]['name']
    print(column_name)
    # query = db_session.query(Base.metadata.tables['basic_user']).filter(getattr(Basic_user, column_name)==1).one()
    # print(query)