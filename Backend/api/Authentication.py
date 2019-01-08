from flask import request
from flask_restful import Resource, abort

from backend.application.Controller.Authentication.Authenticate import Register
from backend.application.Controller.Authentication.Tokens import ValidToken, generate_token


class Auth(Resource):

    # Log User In
    def post(self):
        """

        TODO:

        Take in Username, Optional Password, and Carpool ID
        See if Username Exists in the Carpool Database

        If Exists - See if Password is set and Compare
            If Password matches- Create Token and Return
            Else - Error

        If Doesn't Exist
            Create User
            Store
            Create Token and Return

        :return:
        """

        data = request.json

        print(data)

        # Get Requested Data

        CarpoolID = data.get("CarpoolID")
        Username = data.get("Username")
        Password = data.get("Password")

        print(CarpoolID)

        try:
            Register(CarpoolID, Username, Password)
        except ValueError as e:
            abort(400, description=e.args)

        return {"message": "hello"}

    # Validate Token
    def options(self):

        token = request.headers.get("Authorization").split(" ")[1]

        return {"ValidToken": ValidToken(token)}
