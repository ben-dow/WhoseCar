import datetime

from WhoseCar import db


class Carpool(db.Model):
    id = db.Column(db.String, primary_key=True)
    carpool_name = db.Column(db.String)
    destination = db.Column(db.String)
    description = db.Column(db.String)
    dateAndTime = db.Column(db.DateTime, nullable=False,
                            default=datetime.datetime.now())

    def to_dict(self):

        print()

        return {
            "CarpoolID" : self.id,
            "CarpoolName" : self.carpool_name,
            "Destination" : self.destination,
            "Description" : self.description,
            "Date" : self.dateAndTime.date().strftime("%B %d %Y"),
            "Time": self.dateAndTime.time().strftime("%I:%M %p")
        }
