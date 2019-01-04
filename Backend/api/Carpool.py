from flask import request, jsonify
from flask_restful import Resource, abort
from backend.application.util import id_generator

from backend.application import CreateNewCarpool, FetchExistingCarpoolData


class Carpool(Resource):

    def get(self, id):
        """

        Gets the data associated with a Carpool ID

        :param id:
        :return:
        """


        app_response = FetchExistingCarpoolData(id)

        if "error" in app_response:
            abort(404, description=app_response.get("message"))

        return jsonify(app_response)

    def patch(self, id):
        return {'id': "Done"}

    def options(self, id):

        abort(404)

        return {'id' : "123"}

    def post(self):
        """

        {
        "CarpoolName": "TestName!",
        "Destination": "Place!",
        "Description": "Description!",
        "Datetime" : "YYY-MM-DD:HH:mm:SS
        }


            :return:
        """

        # Extract JSON Data from Request
        r = request.json

        # Have application handle the API Request
        new_carpool_id = CreateNewCarpool(r)

        if new_carpool_id.get("error") is True:
            abort(400, description=new_carpool_id.get("message"))


        return {'id': new_carpool_id.get("id")}, 201
