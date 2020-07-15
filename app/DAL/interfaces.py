from abc import ABCMeta, abstractmethod
from app.DAL.csvReader import CSVReader
from app.DAL.entities import Basic_user, Session, Song, Basic_user_song
from app.DAL.models import BasicUserModel, SongModel, SessionModel, BasicUserSongModel
from app.DAL.dataSaver import DataSaver

class BaseDataAccessLayerInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_csv_data(self): raise NotImplementedError


class DataAccessLayerInterface(BaseDataAccessLayerInterface):
    __metaclass__ = ABCMeta

    FILE_NAME = 'data.csv'
    __csv_reader = CSVReader()
    __data_saver = DataSaver()

    def __init__(self):
        self.csv_reader = DataAccessLayerInterface.__csv_reader
        self.data_saver = DataAccessLayerInterface.__data_saver

    def process_csv_data(self):
        print('DataAccessLayerInterface')

        self.csv_reader.process_csv_file(DataAccessLayerInterface.FILE_NAME)
