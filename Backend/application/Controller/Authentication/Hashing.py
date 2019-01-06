import binascii
import hashlib
from os import urandom


def make_hash(password):
    # Prep Password
    password = password.encode('utf-8')

    # Generate Salt
    salt = hashlib.sha256(urandom(60)).hexdigest().encode('ascii')

    # Hash the Password
    password_hash = hashlib.pbkdf2_hmac('sha512', password, salt, 100000)

    password_hash = binascii.hexlify(password_hash)

    return (salt + password_hash).decode('ascii')


def check_hash(provided_pass, existing_hash):
    # Get info of old pass
    salt = existing_hash[:64]
    hash_a = existing_hash[64:]

    # hash new password
    provided_pass = provided_pass.encode('utf-8')

    hash_b = hashlib.pbkdf2_hmac('sha512', provided_pass, salt.encode('ascii'), 100000)
    hash_b = binascii.hexlify(hash_b).decode('ascii')

    # Compare and Return
    return hash_a == hash_b
