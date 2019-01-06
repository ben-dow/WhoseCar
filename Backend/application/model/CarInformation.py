import datetime

from WhoseCar import db


class Cars(db.Model):
    id = db.Column(db.String, primary_key=True)

    carpool_id = db.Column(db.String, db.ForeignKey('carpool.id'),
                           nullable=False)

    capacity = db.Column(db.Integer, nullable=False)

    time_created = db.Column(db.DateTime, default=datetime.datetime.now())

    carpool = db.relationship('Carpool',
                              backref=db.backref('cars', lazy=True))


class CarParticipants(db.Model):
    user_id = db.Column(db.String, db.ForeignKey('user.id'),
                           nullable=False, primary_key=True)

    carpool_id = db.Column(db.String, db.ForeignKey('carpool.id'),
                           nullable=False, primary_key=True)

    car_id = db.Column(db.String, db.ForeignKey('cars.id'),
                           nullable=False)

    is_driver = db.Column(db.Boolean, nullable=False)

    car = db.relationship('cars.id',
                              backref=db.backref('riders', lazy=True))

    user = db.relationship('User',
                              backref=db.backref('ride_info', lazy=True))
