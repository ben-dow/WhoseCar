from flask import Flask, request, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from CarpoolManagement.Utilities import retrieve_data

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\Benjamin Dow\Desktop\whosecar\whosecar-backend\whosecar.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Templates
from CarpoolManagement.Carpools import Users, Cars, Carpool

# Routes
from CarpoolManagement.CarpoolManagement import PassengerInCarAction, CarpoolActions, CarpoolCarActions, \
    PassengerActions, CarActions, GetPassengersInCar


# Makes sure API Key is correct
def confirm_api_key():
    data = retrieve_data(request)
    api_key = data['api_key']
    if api_key != "hellokey":
        return jsonify({'message': 'API Key Incorrect'})


# Add Api Routes
api.add_resource(CarpoolActions,
                 '/Carpool/NewCarpool',   # Add A new Carpool (POST)
                 '/Carpool/<CarpoolID>')  # Get Carpool Information (GET)


api.add_resource(CarpoolCarActions,
                 '/Carpool/<CarpoolID>/Cars',  # Get the Cars in the Carpool (GET)
                 '/Carpool/<CarpoolID>/AddCar/<PassengerID>',  # Add a Car to the Carpool (POST)
                 '/Carpool/<CarpoolID>/RemoveCar/<CarID>'  # Removes a car from the carpool (DELETE)
                 )
api.add_resource(GetPassengersInCar,
                 '/Cars/<CarID>/Passengers')  # Get List of Passengers in Car (GET)

api.add_resource(PassengerInCarAction,
                 '/Cars/<CarID>/Passengers/AddPassenger/<PassengerID>',  # Add a Passenger to the Car (POST)
                 '/Cars/<CarID>/Passengers/DeletePassenger/<PassengerID>')  # Remove a Passenger from the Car (DELETE)

api.add_resource(PassengerActions,
                 '/Passengers/<PassengerID>',  # Get Information on Passenger (GET)
                 '/Carpool/<CarpoolID>/Passengers/CreatePassenger',  # Create a Passenger (POST)
                 '/Passengers/<PassengerID>/RemovePassenger',  # Remove a Passenger From the System (DELETE)
                 '/Passengers/<PassengerID>/Modify')  # Modify a Passenger in the System with new information (PATCH)

api.add_resource(CarActions,
                 '/Cars/<CarID>')  # Get Information About Car within a carpool(GET)

# Set Up Database
# db.session.query(Carpool).delete()
# db.session.query(Cars).delete()
# db.session.commit()
db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
