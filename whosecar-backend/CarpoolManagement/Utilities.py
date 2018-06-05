import random
import string


def random_b64_string(length):
    res = ''.join(
        random.choice(string.ascii_letters + string.digits + '-' + '_') for i in range(length))
    return res

def retrieve_data(request):
    return request.get_json(force=True)