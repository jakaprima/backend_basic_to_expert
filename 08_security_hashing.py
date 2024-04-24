import hashlib
import bcrypt
import scrypt
import os

list_hash = [
    'md5',
    'sha256',
    'sha384',
    'sha512',
    'bcrypt',
    'scrypt'
]

input_hash = int(input("""
LIST HASH:
list_hash = [
    'md5',
    'sha256',
    'sha384',
    'sha512',
    'bcrypt',
    'scrypt'
]
pilih index ke : 
"""))

match list_hash[input_hash]:
    case "md5":
        hash_object = hashlib.md5()
    case "sha256":
        hash_object = hashlib.sha256()
    case "sha384":
        hash_object = hashlib.sha384()
    case "sha512":
        hash_object = hashlib.sha512()
    case "bcrypt":
        hash_object = "bcrypt"
    case "scrypt":
        hash_object = "scrypt"
    case _:
        print("not valid input")

if hash_object == "bcrypt":
    salt = bcrypt.gensalt()
    password = b"ini plain string asli"
    hashed_password = bcrypt.hashpw(password, salt)

    print("HASH: ", hashed_password)
elif hash_object == "scrypt":
    """
    Scrypt (pronounced “ess crypt”) is a password hashing function (like bcrypt). It is designed to use a lot of hardware, which makes brute-force attacks more difficult. Scrypt is mainly used as a proof-of-work algorithm for cryptocurrencies.
    """
    salt_byte = os.urandom(16)
    password = b"ini plain string asli"
    hashed_password = scrypt.hash(password, salt_byte)
    print('HASH: ', hashed_password)
else:
    string_to_hash = "ini plain string asli"

    # encoding string sebagai byte
    encoded_string = string_to_hash.encode()

    # update hash object dengan byte
    hash_object.update(encoded_string)

    # get hex digest of the hash
    hex_digest = hash_object.hexdigest()

    print("HASH: ", hex_digest)