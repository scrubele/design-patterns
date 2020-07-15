from abc import ABCMeta, abstractmethod
from app.DAL.csvReader import CSVReader
from app.DAL.interfaces import DataAccessLayerInterface


class BaseBusinessLogicLayerInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def process_csv_data(self): raise NotImplementedError


class BusinessLogicLayerInterface(BaseBusinessLogicLayerInterface):
    __metaclass__ = ABCMeta

    FILE_NAME = 'data.csv'
    DAL = DataAccessLayerInterface()

    def process_csv_data(self, DAL: DataAccessLayerInterface):
        print('BusinessLogicLayerInterface')
        self.DAL = DAL
        self.DAL.process_csv_data()

    def save_to_db(self, model_name, value_list):
        self.DAL.data_saver.save_entity_model_by_name_to_db(model_name, value_list)

    def query_all(self, table_name):
        return self.DAL.data_saver.query_all(table_name)

    def remove_object(self, entity_model_name, key, object_id):
        return self.DAL.data_saver.remove_object(entity_model_name, key, object_id)

    def update_object(self, entity_model_name, key, object_id, values):
        return self.DAL.data_saver.update_user(entity_model_name, key, object_id, values)