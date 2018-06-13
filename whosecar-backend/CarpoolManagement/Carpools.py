from whosecar import db


class Carpool(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    Title = db.Column(db.String(64))
    DateCreated = db.Column(db.TIMESTAMP)

    Cars = db.relationship('Cars', backref='carpool', lazy=True)
    Users = db.relationship('Users', backref='carpool', lazy=True)

    def toJson(self):
        json ={
            'id': self.id,
            'Title': self.Title,
            'Cars': {},
            'Users': {}
        }

        for c in self.Cars:
            json['Cars'][c.id] = c.toJson()

        for u in self.Users:
            json['Users'][u.id] = u.toJson()

        return json


class Cars(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    CarCapacity = db.Column(db.Integer)
    TimeCreated = db.Column(db.TIMESTAMP)
    carpool_id = db.Column(db.String(8), db.ForeignKey('carpool.id'))
    owner_id = db.Column(db.String(8))

    Passengers = db.relationship('Users', backref='cars', lazy=True)

    def toJson(self):
        json = {
            'id': self.id,
            'CarCapacity': self.CarCapacity,
            'Carpool_ID': self.carpool_id,
            'Owner_ID':self.owner_id,
            'Passengers': [],
            'Owner_Name': Users.query.filter_by(id=self.owner_id).first().PassengerName
        }
        for p in self.Passengers:
            json['Passengers'].append(p.toJson())
        return json




class Users(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    car_id = db.Column(db.String(8), db.ForeignKey('cars.id'))
    carpool_id = db.Column(db.String(8), db.ForeignKey('carpool.id'))
    driver = db.Column(db.Boolean)
    TimeSelected = db.Column(db.TIMESTAMP)
    PassengerName = db.Column(db.String(24))

    def toJson(self):
        json ={
            'id': self.id,
            'Car_ID': self.car_id,
            'Carpool_ID': self.carpool_id,
            'Driver': self.driver,
            'Name': self.PassengerName
        }
        return json