import os
from datetime import datetime, timedelta
import jwt


def generate_token(user_id, carpool_id):
    token = jwt.encode(
        {
            "CarpoolID": carpool_id,
            "UserID": user_id,
            "TokenExpiration": (datetime.now() + timedelta(hours=1)).isoformat()  # Token Valid for 1 Hour
        },
        os.getenv('jwtSecret'),
        algorithm="HS256"
    )

    return token


def ValidToken(token):
    decoded_token = decode_token(token)

    token_keys = decoded_token.keys()

    if len(token_keys) != 3:
        # Make sure only 3 values in the payload
        return False

    if "TokenExpiration" not in token_keys and "CarpoolID" not in token_keys and "UserID" not in token_keys:
        # Make sure the Payload has correct Values
        return False

    if datetime.fromisoformat(decoded_token.get("TokenExpiration")) < datetime.now(): # Check if the Token has Exipred
        return False



    return True




def decode_token(token):

    return jwt.decode(token, os.getenv('jwtSecret'), algorithms=['HS256'])

