import datetime
import time

from flask import request
from flask_restful import Resource

from CarpoolManagement.Carpools import Carpool, Cars, CarPassengers
from CarpoolManagement.Utilities import random_b64_string, retrieve_data
from whosecar import db


class NewCarpool(Resource):
    def get(self,CarpoolID):
        c = Carpool.query.filter_by(id=CarpoolID).first()
        print(c.Cars)
        carpool_dict = {
            'id': c.id,
            'Title': c.Title,
            'TimeCreated': c.DateCreated.__str__(),
            'NumberCars': c.Cars.__len__(),
        }
        return carpool_dict

    def post(self,CarpoolID):
        data = request.get_json(force=True)
        data = data['CarpoolName']

        carpool_i_d = random_b64_string(8)
        while Carpool.query.filter_by(id=carpool_i_d).first() is not None:
            carpool_i_d = random_b64_string(8)

        db.session.add(Carpool(id=carpool_i_d, Title=data, DateCreated=datetime.datetime.now()))
        db.session.commit()

        return {'url': carpool_i_d}


class Car(Resource):
    def get(self, CarpoolID):
        cars = Cars.query.filter_by(carpool_id=CarpoolID).all()
        car_dict = {}

        for c in cars:
            car_dict[c.OwnerName] = {
                'OwnerName': c.OwnerName,
                'CarCapacity': c.CarCapacity,
                'TimeCreated': c.TimeCreated.__str__(),
                'CarID': c.id,
                'Passengers': c.Passengers
            }
        return car_dict

    def post(self, CarpoolID):
        carpool = Carpool.query.filter_by(id=CarpoolID).first()

        if carpool is None:
            return {'message': 'Carpool ID was not found'}
        data = retrieve_data(request)

        car_id = random_b64_string(8)
        while Cars.query.filter_by(id=car_id).first() is not None:  # Guarantees Unique ID
            car_id = random_b64_string(8)

        owner_name = data['owner_name']
        car_capacity = data['car_capacity']
        time_created = datetime.datetime.now()

        CarCheck = Cars.query.filter((Cars.OwnerName == owner_name) & (Cars.carpool_id == CarpoolID))
        if len(CarCheck.all()) > 0:
            car = CarCheck.first()
            car.CarCapacity = car_capacity
            return {'CarID': car.id, 'message': 'Car Updated'}

        car = Cars(id=car_id, OwnerName=owner_name, CarCapacity=car_capacity,
                   TimeCreated=time_created, carpool_id=CarpoolID)

        db.session.add(car)
        db.session.commit()

        return {'CarID': car_id}


class PassengersByCar(Resource):
    def get(self, CarID):
        passengers = CarPassengers.query.filter_by(car_id=CarID).all()
        passenger_dict = {}

        for p in passengers:
            passenger_dict[p.PassengerName] = {
                'PassengerName': p.PassengerName,
                'TimeCreated': p.TimeSelected.__str__(),
                'CarID': p.car_id
            }
        return passenger_dict

    def post(self, CarID):

        car_check = Cars.query.filter_by(id=CarID).first()

        if car_check == None:
            return {'message': 'Car not found'}
        data = retrieve_data(request)
        passenger_name = data['passenger_name']

        passenger_check = CarPassengers.query.filter(
            (CarPassengers.PassengerName == passenger_name) & (CarPassengers.car_id == CarID))  # Checks to see if
        # passenger is already in the car

        carpool = Carpool.query.filter_by(id=car_check.carpool_id).first()

        for c in carpool.Cars:
            for p in c.Passengers:
                if p.PassengerName == passenger_name:
                    return {'message': 'Passenger already in a Car'}

        new_passenger = CarPassengers(car_id = CarID, TimeSelected=datetime.datetime.now(),PassengerName=passenger_name)

        db.session.add(new_passenger)
        db.session.commit()

        return {'message': 'Passenger Added'}