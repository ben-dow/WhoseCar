import datetime

from flask import request, jsonify
from flask_restful import Resource, abort

from CarpoolManagement.Carpools import Carpool, Cars, Users
from CarpoolManagement.Utilities import random_b64_string, retrieve_data
from whosecar import db


class CarpoolActions(Resource):
    def get(self, carpool_i_d: str) -> dict:
        c = Carpool.query.filter_by(id=carpool_i_d).first()  # Fetch the Carpool from DB

        if c is None:  # Confirm Carpool Exists
            abort(400, description="CarpoolID Not Found")

        carpool_dict = {
            'id': c.id,
            'Title': c.Title,
            'TimeCreated': c.DateCreated.__str__(),
            'NumberCars': c.Cars.__len__(),
        }

        return carpool_dict

    def post(self) -> dict:
        data = retrieve_data(request)['CarpoolName']  # Fetch the Data and extract the key

        carpool_i_d = random_b64_string(8)  # Generate Random ID For the Carpool

        while Carpool.query.filter_by(
                id=carpool_i_d).first() is not None:  # Make sure the ID Doesnt exist in the DB already
            carpool_i_d = random_b64_string(8)

        db.session.add(
            Carpool(id=carpool_i_d,
                    Title=data,
                    DateCreated=datetime.datetime.now()))  # Create instance of Carpool and add it to the DB
        db.session.commit()  # Commit the Changes to the DB

        return {'url': carpool_i_d}


class CarpoolCarActions(Resource):
    def get(self, CarpoolID):
        carpool_check = Carpool.query.filter_by(id=CarpoolID).first()

        if carpool_check is None:
            abort(400, description="CarpoolID Not Found")

        cars = Cars.query.filter_by(carpool_id=CarpoolID).all()
        car_dict = {}

        for c in cars:
            car_dict[c.id] = {
                'CarCapacity': c.CarCapacity,
                'TimeCreated': c.TimeCreated.__str__(),
                'CarID': c.id,
                'Passengers': []
            }

            for p in c.Passengers:
                car_dict[c.OwnerName]["Passengers"].append(p.id)
                if p.driver:
                    car_dict[c.id]['OwnerID'] = p.id

        return car_dict

    def post(self, CarpoolID, PassengerID):
        carpool = Carpool.query.filter_by(id=CarpoolID).first()

        if carpool is None:
            abort(400, description='Carpool ID was not found')
        data = retrieve_data(request)

        car_id = random_b64_string(8)
        while Cars.query.filter_by(id=car_id).first() is not None:  # Guarantees Unique ID
            car_id = random_b64_string(8)

        car_capacity = data['car_capacity']
        time_created = datetime.datetime.now()

        passenger = Users.query.filter_by(id=PassengerID).first()

        if passenger is None:
            abort(400, description='Owner ID was not found')

        car = Cars(id=car_id, CarCapacity=car_capacity,
                   TimeCreated=time_created, carpool_id=CarpoolID, owner_id=PassengerID)

        passenger.car_id = car_id
        passenger.driver = True

        db.session.add(car)
        db.session.commit()

        return {'CarID': car_id}

    def delete(self, CarpoolID, CarID):
        carpool = Carpool.query.filter_by(id=CarpoolID).first()
        if carpool is None:
            return abort(400, description='Carpool ID was not found')

        car = Cars.query.filter_by(id=CarID).first()

        if car is None:
            return abort(400, description='Car ID was not found')

        db.session.delete(car)
        db.session.commit()
        return {'message': "Car id " + CarID + " was deleted from carpool " + CarpoolID}


class GetPassengersInCar(Resource):
    def get(self, CarID):
        car_check = Cars.query.filter_by(id=CarID)

        if car_check is None:
            abort(400, description="CarID not Found")

        passengers = Users.query.filter_by(car_id=CarID).all()

        passenger_dict = {}

        for p in passengers:
            passenger_dict[p.PassengerName] = {
                'PassengerName': p.PassengerName,
                'PassengerID': p.id,
                'TimeCreated': p.TimeSelected.__str__(),
                'CarID': p.car_id
            }
        return jsonify(passenger_dict)


class PassengerInCarAction(Resource):
    def post(self, CarID, PassengerID):
        car_check = Cars.query.filter_by(id=CarID).first()

        if car_check is None:
            abort(400, description="CarID Not Found")

        pass_check = Users.query.filter_by(id=PassengerID).first()
        if pass_check is None:
            abort(400, description="UserID Not found")

        if car_check.CarCapacity == len(car_check.Passengers):
            abort(400, description="Car is at Capacity")

        pass_check.car_id = CarID
        pass_check.TimSelected = datetime.datetime.now()
        db.session.commit()
        return {'message': "User " + PassengerID + " was added to the car " + CarID}

    def delete(self, CarID, PassengerID):
        car_check = Cars.query.filter_by(id=CarID).first()

        if car_check is None:
            abort(400, description="CarID Not Found")

        pass_check = Users.query.filter_by(id=PassengerID).first()
        if pass_check is None:
            abort(400, description="UserID Not found")

        pass_check.car_id = None

        db.session.commit()
        return {'message': "User " + PassengerID + " was removed from the car " + CarID}


class PassengerActions(Resource):
    def get(self, PassengerID):
        pass_check = Users.query.filter_by(id=PassengerID).first()

        if pass_check == None:
            abort(400, description="PassengerID Not Found")

        info = {
            'id': pass_check.id,
            'car_id': pass_check.car_id,
            'driver': pass_check.driver,
            'TimeSelected': pass_check.TimeSelected.__str__(),
            'Name': pass_check.PassengerName
        }

        return info

    def post(self, CarpoolID):

        carpool_check = Carpool.query.filter_by(id=CarpoolID).first()

        if carpool_check is None:
            abort(400, description="CarID Not Found")

        data = retrieve_data(request)
        passenger_name = data['passenger_name']

        passenger_check = Users.query.filter(
            (Users.PassengerName == passenger_name) & (Users.carpool_id == CarpoolID))  # Checks to see if
        # passenger is already in the carpool
        if passenger_check.first() is not None:
            abort(400, description="Passenger already exists in the carpool")

        passenger_id = random_b64_string(8)
        new_passenger = Users(id=passenger_id, car_id=None, TimeSelected=datetime.datetime.now(),
                              PassengerName=passenger_name, carpool_id=CarpoolID)

        db.session.add(new_passenger)
        db.session.commit()

        return {'message': 'Passenger Added', 'PassengerID': passenger_id}

    def patch(self, PassengerID):
        pass_check = Users.query.filter_by(id=PassengerID).first()

        if pass_check is None:
            abort(400, description="PassengerID Not Found")

        data = retrieve_data(request)

        pass_check.driver = data['driver']

        db.session.commit()

        return {'message': 'Passenger Modified'}


class CarActions(Resource):
    def get(self, CarID):
        car_check = Cars.query.filter_by(id=CarID).first()

        if car_check is None:
            abort(400, description="CarID Not Found")

        info = {
            "id": car_check.id,
            "CarCapacity": car_check.CarCapacity,
            "TimeCreated": car_check.TimeCreated.__str__(),
            "CarpoolID": car_check.carpool_id,
            "Passengers": []

        }

        for p in car_check.Passengers:
            info["Passengers"].append(p.id)

        return info
