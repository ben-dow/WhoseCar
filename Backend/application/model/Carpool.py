import datetime

from WhoseCar import db


class Carpool(db.Model):
    id = db.Column(db.String, primary_key=True)
    carpool_name = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    time_of_carpool = db.Column(db.DateTime, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now())

    def to_dict(self):

        print()

        return {
            "CarpoolID" : self.id,
            "CarpoolName" : self.carpool_name,
            "Destination" : self.destination,
            "Description" : self.description,
            #"Date" : self.time_of_carpool.date().strftime("%B %d %Y"),
            #"Time": self.time_of_carpool.time().strftime("%I:%M %p")
        }
