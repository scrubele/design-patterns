
# from app import app
import csv
from app.DAL.models import BasicUserModel, SongModel, SessionModel, BasicUserSongModel
from app.database import db_session, Base
from app.DAL.entities import Basic_user, Song, Session, Basic_user_song

class DataSaver:

    def save_model_data(self, entity_model_instance):
        entity_model_instance.init_table_value()

    def create_entity_object(self, entity_model_name, values):
        entity_model = globals()[entity_model_name]
        return entity_model(*values)

    def save_entity_model_by_name_to_db(self, entity_model, values):
        entity_model_instance = self.create_entity_object(entity_model, values)
        entity_model_instance.init_table_value()
        print(entity_model+" data saved")

    def save_entity_model_to_db(self, entity_model, values):
        entity_model_instance = entity_model(*values)
        entity_model_instance.init_table_value()

    def query_all(self, table_name):
        # print(Base.metadata.tables)
        return db_session.query(Base.metadata.tables[table_name]).all()

    def remove_object(self, entity_model_name, key, object_id):
        print(object_id)
        entity_model = globals()[entity_model_name]
        # removing from many-to-many table, e.g.: Basic_user_song and basic_user_id
        db_session.query(Basic_user_song).filter(getattr(Basic_user_song, key)==object_id).delete()
        db_session.query(entity_model).filter(getattr(entity_model, key)==object_id).delete()
        db_session.commit()

    def update_user(self, entity_model_name, key, object_id, values):
        print(object_id)
        entity_model = globals()[entity_model_name]       
        db_session.query(entity_model).filter(getattr(entity_model, key)==object_id).update(values)