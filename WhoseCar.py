import os
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

'''
Load Environment Configuration
'''
env_path = Path('.') / 'whosemyride.env'
load_dotenv(dotenv_path=env_path)


'''
Initiate Flask App
'''
app = Flask(__name__, static_folder='frontend/build')
cors = CORS(app, origin="http://127.0.0.1:5000")


'''
Configure Database
'''
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DatabaseLocation")
db = SQLAlchemy(app)

from backend.application.model import *

''' API Setup'''

api = Api(app)
from backend.api.Setup import *


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
