from backend.application.util import id_generator
from backend.application.model import DBUpdater
from backend.application.model import Carpool

from datetime import datetime


def CreateNewCarpool(initial_carpool_data: dict) -> dict:
    # Expected Data
    expected_data = ['CarpoolName', 'Destination', 'Description', 'Datetime']
    expected_data = set(expected_data)

    # Verify Correct Data Exists
    keys = initial_carpool_data.keys()
    keys = set(keys)

    if keys != expected_data:
        return {"id": None, "error": True, "message": "Incorrect Data Keys"}

    # Construct New Carpool Object
    generated_id = id_generator()

    c = Carpool(id=generated_id,
                carpool_name=initial_carpool_data.get('CarpoolName'),
                destination=initial_carpool_data.get('Destination'),
                description=initial_carpool_data.get('Description'),
                dateAndTime= datetime.strptime(initial_carpool_data.get('Datetime'), '%Y-%m-%d %H:%M'))

    DBUpdater([c])

    return {"id": id_generator(), "error": False, "message": "Success"}


def UpdateCarpoolData(updated_carpool_data):
    return True


def FetchExistingCarpoolData(carpool_id):
    return {}
