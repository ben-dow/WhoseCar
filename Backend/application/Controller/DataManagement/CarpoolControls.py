from backend.application.util import id_generator


def CreateNewCarpool(initial_carpool_data):
    return id_generator()


def UpdateCarpoolData(updated_carpool_data):
    return True


def FetchExistingCarpoolData(carpool_id):
    return {}