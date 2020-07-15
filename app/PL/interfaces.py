from abc import ABCMeta, abstractmethod
from app.DAL.csvReader import CSVReader
from app.DAL.interfaces import DataAccessLayerInterface


class BasePresentationalLevelInterface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_views(self): raise NotImplementedError


class PresentationalLevelInterface(BasePresentationalLevelInterface):
    __metaclass__ = ABCMeta
    
    def init_views(self, BLL):
        from app.PL.views import UserView, DataView
        self.BLL = BLL
        self.DataView = DataView
        self.DataView.BLL = BLL

        
