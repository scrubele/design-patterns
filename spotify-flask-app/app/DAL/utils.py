from marshmallow_sqlalchemy import ModelSchema

def add_schema(cls):
    class Schema(ModelSchema):
        class Meta:
            model = cls
    cls.Schema = Schema
    return cls