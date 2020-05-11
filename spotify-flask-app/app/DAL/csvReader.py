# from app import app
import csv
from app.DAL.models import BasicUserModel, SongModel, SessionModel, BasicUserSongModel
from app.DAL.dataSaver import DataSaver

class FileContextManager:

    def __init__(self, file_name, access_mode):
        self.file_name = file_name
        self.access_mode = access_mode
        self.file = open(file_name, access_mode)
        self.reader = csv.reader(self.file)

    def __iter__(self):
        return self

    def __enter__(self):
        return self

    def __next__(self):
        self.current = next(self.reader)
        return self

    def __exit__(self, **args):
        end = True


class CSVReader(DataSaver):

    CLASS_NAME = 1
    MODEL = "Model"

    def get_row_data(self, values):
        return values[CSVReader.CLASS_NAME:]
        
    def process_csv_file(self, csv_file_name):
        entity_model_name = str

        for reader in FileContextManager(csv_file_name, 'r'):
            row = reader.current
            values_number = len(row)
            if (values_number == CSVReader.CLASS_NAME):
                entity_model_name = row[CSVReader.CLASS_NAME-1].split(':')[CSVReader.CLASS_NAME] + CSVReader.MODEL
                print(entity_model_name)
            elif(values_number > 0):
                values = self.get_row_data(row)
                entity_model_instance = self.create_entity_object(entity_model_name, values)
                self.save_model_data(entity_model_instance)

