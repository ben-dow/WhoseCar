import datetime

from WhoseCar import db


class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    carpool_id = db.Column(db.String, db.ForeignKey('carpool.id'),
                           nullable=False)
    username = db.Column(db.String, nullable=False)

    password = db.Column(db.String)

    salt = db.Column(db.Integer)

    admin = db.Column(db.Boolean, default=False, nullable=False)

    display_name = db.Column(db.String)

    notes = db.Column(db.String)

    contact_info = db.Column(db.String)

    # Valid Participant Types are NONE, DRIVER, RIDER
    participant_type = db.Column(db.String, default="NONE", nullable=False)

    date_added = db.Column(db.DateTime, default=datetime.datetime.now())

    carpool = db.relationship('Carpool',
                               backref=db.backref('users', lazy=True))
