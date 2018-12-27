import os

from flask import Flask, make_response, send_from_directory
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__, static_folder='frontend/build')
api = Api(app)

cors = CORS(app, allow_headers='Content-Type')

app.config['CORS_HEADERS'] = 'Content-Type'

from backend.api import Carpool
api.add_resource(Carpool, '/api/Carpool', '/api/Carpool/<id>')

''' Serve React App'''

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("frontend/build/" + path):
        return send_from_directory('frontend/build', path)
    else:
        return send_from_directory('frontend/build', 'index.html')




if __name__ == '__main__':
    app.run()
