import datetime

from WhoseCar import db


class Carpool(db.Model):
    id = db.Column(db.String, primary_key=True)
    carpool_name = db.Column(db.String)
    destination = db.Column(db.String)
    description = db.Column(db.String)
    dateAndTime = db.Column(db.DateTime, nullable=False,
                            default=datetime.datetime.now())

