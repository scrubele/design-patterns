from app.DAL.entities import Basic_user, Song, Session, Basic_user_song
from app import db
from app.database import db_session, Base
from abc import ABCMeta, abstractmethod

class DataModelInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self): raise NotImplementedError

    @abstractmethod
    def init_table_value(self): raise NotImplementedError

    @abstractmethod
    def add_to_db(self): raise NotImplementedError


class DataModel(DataModelInterface):

    def __init__(self):
        pass

    def init_table_value(self):
        pass

    def add_to_db(self):
        db_session.add(self.object)
        db_session.commit()

    def check_existance(self, table_name, entity_name, key):
        column_name = db_session.query(Base.metadata.tables[table_name]).column_descriptions[0]['name']
        query = db_session.query(Base.metadata.tables[table_name]).filter()
        entity_model = globals()[entity_name]
        query = db_session.query(Base.metadata.tables[table_name]).filter(getattr(entity_model, column_name)==key).filter
        if(len(query)>0):
            return True
        return False
         
class BasicUserModel(DataModel):
    """Data model for user accounts."""

    def __init__(self, email, country, age,  songs=None, sessions=None):
        self.email = email
        self.age = age
        self.country = country
        self.songs = songs
        self.sessions = sessions
    
    def init_table_value(self):
        self.object = Basic_user(email=self.email, age=self.age, country=self.country)
        # if self.songs is not None:
        #     self.object.songs.add(self.songs)
        # if self.sessions is not None:
        #     self.object.sessions.add(self.sessions)           
        self.add_to_db()

class SongModel(DataModel):
    """Data model for song."""

    def __init__(self, name, length, rating, users=None, sessions=None):
        self.name = name
        self.length = length
        self.rating = rating
        self.users = users
        self.sessions = sessions
        self.init_table_value()
    
    def init_table_value(self):
        self.object = Song(name=self.name, length=self.length, rating=self.rating)
        # if self.users is not None:
        #     self.object.add(self.users)
        # if self.sessions is not None:
        #     self.object.add(self.sessions)        
        self.add_to_db()

class SessionModel(DataModel):
    """Data model for session."""

    def __init__(self, day, month, year, duration, songs=None, users=None):
        self.day = day
        self.month = month
        self.year = year
        self.duration = duration
        self.users = users
        self.songs = songs
        self.init_table_value()
    
    def init_table_value(self):
        self.object = Session(day=self.day, month=self.month, year=self.year, duration=self.duration)
        # if self.songs is not None:
        #     self.object.add(self.songs)
        # if self.users is not None:
        #     self.object.add(self.users)        
        self.add_to_db()

class BasicUserSongModel(DataModel):
    """Data model for session."""

    def __init__(self, basic_user_id, song_id, session_id, songs=None, users=None):
        self.basic_user_id = basic_user_id
        self.song_id = song_id
        self.session_id = session_id
    
    def init_table_value(self):
        self.object = Basic_user_song(basic_user_id=self.basic_user_id, song_id=self.song_id, session_id=self.session_id) 
        does_exists = self.check_row_existance("basic_user_song", "Basic_user_song", [self.basic_user_id, self.song_id, self.session_id]) 
        if not does_exists:   
            self.add_to_db()


    def check_row_existance(self, table_name, entity_name, keys):
        row_query = db_session.query(Base.metadata.tables[table_name]).filter(getattr(Basic_user_song, "basic_user_id")==keys[0])\
                                                                  .filter(getattr(Basic_user_song, "song_id")==keys[1])\
                                                                .filter(getattr(Basic_user_song, "session_id")==keys[2]).all()  
        try:
            if(len(row_query)>0):                                   
                return True
        except TypeError:
            return False
        return False