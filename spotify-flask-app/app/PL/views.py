from flask import request, render_template, make_response, Response
from datetime import datetime as dt
from flask import current_app as app, jsonify
from flask.views import View
from app.DAL.entities import Basic_user, Song, Session, Basic_user_song
from flask_cors import CORS, cross_origin
from abc import ABCMeta, abstractmethod


class ViewInterface(View):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(): raise NotImplementedError

    @abstractmethod
    def post(): raise NotImplementedError

    @abstractmethod
    def put(): raise NotImplementedError

    @abstractmethod
    def delete(): raise NotImplementedError


class DataView(ViewInterface):

    entites = list
    models = list
    Basic_user = 0
    Song = 1
    Session = 2
    Basic_user_song = 3


class UserView(DataView):

    @cross_origin
    @app.route('/users', methods=['GET'])
    def get():
        data = DataView.BLL.query_all("basic_user")
        # print(data)
        return jsonify(json_list=data)

    @cross_origin
    @app.route('/users', methods=['POST'])
    def post():
        data = dict(request.form)
        print(data)
        value_list = [value for key, value in data.items()]
        DataView.BLL.save_to_db("BasicUserModel", value_list)
        print(value_list)
        # json_data = request.form.get('json_data')
        return jsonify(value_list)

    @cross_origin
    @app.route('/users/<object_id>', methods=['Delete'])
    def delete(object_id):
        print(object_id)

        DataView.BLL.remove_object("Basic_user", "basic_user_id", object_id)
        return {'object': 'removed'}


    @cross_origin
    @app.route('/users/<object_id>', methods=['Put'])
    def put(object_id):
        data = dict(request.form)
        DataView.BLL.update_object("Basic_user", "basic_user_id", object_id, data)
        return {'object': 'updated'}
