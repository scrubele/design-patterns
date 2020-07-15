from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from .database import init_db
from flask_marshmallow import Marshmallow
from flask_cors import CORS, cross_origin
from config import Config
db = SQLAlchemy()
Base = declarative_base()

def init_levels():
    from app.DAL.interfaces import DataAccessLayerInterface
    from app.BLL.interfaces import BusinessLogicLayerInterface
    from app.PL.interfaces import PresentationalLevelInterface
    DAL = DataAccessLayerInterface()
    BLL = BusinessLogicLayerInterface()
    PL = PresentationalLevelInterface()
    return DAL, BLL, PL

app = Flask(__name__, instance_relative_config=False)
app.config.from_object(Config)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
db.init_app(app)
ma = Marshmallow(app)

with app.app_context():

    DAL, BLL, PL = init_levels()
    # BLL.process_csv_data(DAL)
    init_db()
    PL.init_views(BLL)
