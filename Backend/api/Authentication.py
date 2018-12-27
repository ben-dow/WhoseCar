import os
import time

from flask import request
from flask_restful import Resource
import jwt

from backend.application.Authentication.Tokens import ValidToken, generate_token

class Auth(Resource):

    #Log User In
    def post(self):
        '''

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
        '''

        token = generate_token("12345", "412uo")

        return {'token' : token.decode('utf-8')}

    # Validate Token
    def options(self):
        data = request.json.get("token")

        print(ValidToken(data))



        return {'Data':"123"}






