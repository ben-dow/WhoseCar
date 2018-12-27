from flask import request
from flask_restful import Resource, abort
from backend.application.util import id_generator


class Carpool(Resource):

    def get(self, id):
        '''

        Gets the data associated with a Carpool ID

        :param id:
        :return:
        '''

        return{'id' : 1234}

    def post(self):
        return {'id' : id_generator()}

    def head(self, id):
        abort(404)
        return {'id' : id_generator()}

