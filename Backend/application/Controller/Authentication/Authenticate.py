import hashlib, binascii

from backend.application.model import User
from backend.application.model import Carpool


def Authenticate(CarpoolID, Username, Password):
    pass


def Register(CarpoolID, Username, Password):
    # Get list of Users in Carpool

    carpool = Carpool.query.filter_by(id=CarpoolID).first()

    if carpool is None:
        raise ValueError("Carpool ID does not exist")

    carpool.users.filter_by(id="1").all()


