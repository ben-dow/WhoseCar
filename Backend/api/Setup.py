from WhoseCar import api
from backend.api.Carpool import Carpool
from backend.api.Authentication import Auth

''' Carpool '''
api.add_resource(Carpool, '/api/Carpool', '/api/Carpool/<id>')

''' Authentication '''
api.add_resource(Auth, '/api/Authentication')


''' Driver '''

''' Rider '''

''' User Settings '''

