from flask import request
from flask_restful import Resource, abort
from backend.application.util import id_generator

from backend.application import CreateNewCarpool


class Carpool(Resource):

    def get(self, id):
        """

        Gets the data associated with a Carpool ID

        :param id:
        :return:
        """

        return {'id': 1234}

    def patch(self, id):
        return {'id': "Done"}

    def post(self):
        """

        {
        "CarpoolName": "TestName!",
        "Destination": "Place!",
        "Description": "Description!",
        "Date": "yyy-mm-dd",
        "Time": "hh-mm"
        }




            :return:
        """

        # Extract JSON Data from Request
        r = request.json

        # Have application handle the API Request
        new_carpool_id = CreateNewCarpool(r)

        return {'id': new_carpool_id}, 201
