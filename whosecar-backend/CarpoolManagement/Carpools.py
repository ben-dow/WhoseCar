from whosecar import db


class Carpool(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    Title = db.Column(db.String(64))
    DateCreated = db.Column(db.TIMESTAMP)

    Cars = db.relationship('Cars', backref='carpool', lazy=True)
    Users = db.relationship('Users', backref='carpool', lazy=True)


class Cars(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    CarCapacity = db.Column(db.Integer)
    TimeCreated = db.Column(db.TIMESTAMP)
    carpool_id = db.Column(db.String(8), db.ForeignKey('carpool.id'))
    owner_id = db.Column(db.String(8))

    Passengers = db.relationship('Users', backref='cars', lazy=True)


class Users(db.Model):
    id = db.Column(db.String(8), primary_key=True)
    car_id = db.Column(db.String(8), db.ForeignKey('cars.id'))
    carpool_id = db.Column(db.String(8), db.ForeignKey('carpool.id'))
    driver = db.Column(db.Boolean)
    TimeSelected = db.Column(db.TIMESTAMP)
    PassengerName = db.Column(db.String(24))
