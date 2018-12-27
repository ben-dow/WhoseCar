from flask_restful import Resource

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
        
        return {'token' : '123asdhfjaksdf'}

    # Validate Token
    def head(self):
        




