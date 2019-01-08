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
                time_of_carpool=datetime.strptime(initial_carpool_data.get('Datetime'), '%Y-%m-%d %H:%M'))

    update = DBUpdater([c])

    if update is True:
        return {"id": generated_id, "error": False, "message": "Success"}
    else:
        return {"id": None, "error": True, "message": "Unknown Error"}


def UpdateCarpoolData(updated_carpool_data):
    pass


def FetchExistingCarpoolData(carpool_id):
    # Query For Item
    item = Carpool.query.filter_by(id=carpool_id).first()

    # Abort if Item is None

    if item is None:
        return {"error": True, "message": "Carpool with id {0} Not Found".format(carpool_id)}

    print(item.users)

    return item.to_dict()
