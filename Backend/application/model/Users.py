from WhoseCar import db


class User(db.Model):

    id = db.Column(db.String, primary_key=True)