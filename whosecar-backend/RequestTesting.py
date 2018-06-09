import json

import requests

url = "http://localhost:5000/"


def PostRequest(urlext, data):
    r = requests.post(url + urlext, json=data)
    return r


def DeleteRequest(urlext, data):
    r = requests.delete(url + urlext, json=data)
    return r


def GetRequest(urlext, data):
    r = requests.get(url + urlext, json=data)
    return r


def CreateCarpool():
    r = PostRequest('Carpool/NewCarpool', {'CarpoolName': "A Testing Carpool"})
    data = json.loads(r.text)
    return data['url']


def CarpoolInfo(id):
    r = GetRequest('Carpool/' + id, {})
    print(r.text)


def AddPassenger(carpoolid, name):
    passdata = {
        'passenger_name': name
    }
    r = PostRequest('Carpool/' + carpoolid + '/Passengers/CreatePassenger', passdata)
    data = json.loads(r.text)
    return data['PassengerID']


def ViewPassengerInformation(passid):
    r = GetRequest('Passengers/' + passid, {})
    print(r.text)


def AddCar(CarpoolID, PassengerID, Capacity):
    r = PostRequest('Carpool/' + CarpoolID + '/AddCar/' + PassengerID, {'car_capacity': Capacity})
    data = json.loads(r.text)
    return (data['CarID'])


def GetCarInfo(CarID):
    r = GetRequest('Cars/' + CarID, {})
    data = json.loads(r.text)
    print(data)


def AddPassengerToCar(CarID, PassengerID):
    r = PostRequest('Cars/' + CarID + '/Passengers/AddPassenger/' + PassengerID, {})
    print(r.url)
    data = json.loads(r.text)
    print(data)


def ViewPassengers(CarID):
    r = GetRequest('Cars/' + CarID + '/Passengers', {})
    data = json.loads(r.text)
    print(data)
