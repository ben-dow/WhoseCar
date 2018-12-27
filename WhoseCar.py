import os
from pathlib import Path

from flask import Flask, make_response, send_from_directory
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv


app = Flask(__name__, static_folder='frontend/build')
api = Api(app)
cors = CORS(app, origin="http://127.0.0.1:5000")

'''
Load Environment Configuration
'''
env_path = Path('.') / 'whosemyride.env'
load_dotenv(dotenv_path=env_path)

''' API Setup'''
from backend.api import Setup

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
