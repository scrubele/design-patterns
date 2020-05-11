from app import db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.database import Base
from app.DAL.utils import add_schema


class Basic_user(Base):
    """Data model for user accounts."""

    __tablename__ = 'basic_user'
    basic_user_id = db.Column(db.Integer,
                   primary_key=True)
    email = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    password = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    age = db.Column(db.Integer,
                    index=False,
                    unique=False,
                    nullable=True)
    country = db.Column(db.String(80),
                      index=False,
                      unique=False,
                      nullable=False)
    songs = relationship('Song', secondary = 'basic_user_song')
    sessions = relationship('Session', secondary = 'basic_user_song')

    def __repr__(self):
        return '<BasicUser {}>'.format(self.email)
    
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'basic_user_id':self.basic_user_id
       }


class Song(Base):
    """Data model for songs."""

    __tablename__ = 'song'
    song_id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    length = db.Column(db.Integer,
                      index=True,
                      unique=True,
                      nullable=False)
    rating = db.Column(db.Integer,
                    index=False,
                    unique=False,
                    nullable=True)
    users = relationship('Basic_user', secondary = 'basic_user_song')
    sessions = relationship('Session', secondary = 'basic_user_song')
                
    def __repr__(self):
        return '<Song {}>'.format(self.name)


class Session(Base):
    """Data model for sessions."""

    __tablename__ = 'session'
    session_id = db.Column(db.Integer,
                   primary_key=True)
    day = db.Column(db.String(64),
                         index=False,
                         unique=True,
                         nullable=False)
    month = db.Column(db.Integer,
                      index=True,
                      unique=True,
                      nullable=False)
    year = db.Column(db.Integer,
                    index=False,
                    unique=False,
                    nullable=True)
    duration = db.Column(db.Integer,
                index=False,
                unique=False,
                nullable=True)
    songs = relationship('Song', secondary = 'basic_user_song')
    users = relationship('Basic_user', secondary = 'basic_user_song')

    def __repr__(self):
        return '<Session {}>'.format(self.session_id)



class Basic_user_song(Base):
    """Data model for sessions."""

    __tablename__ = 'basic_user_song'
    basic_user_id = db.Column(db.Integer,
                   ForeignKey('basic_user.basic_user_id'), 
                   primary_key=True)
    song_id = db.Column(db.Integer,
                   ForeignKey('song.song_id'), 
                   primary_key=True)
    session_id = db.Column(db.Integer,
                   ForeignKey('session.session_id'), 
                   primary_key=True)
