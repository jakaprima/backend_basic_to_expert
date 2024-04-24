"""
JSON WEB TOKEN : 
is an open standard (RFC 7519) that defines a compact and self-contained way for securely 
transmitting information between parties as a JSON object. This information can be 
verified and trusted because it is digitally signed. JWTs can be signed using a secret 
(with the HMAC algorithm) or a public/private key pair using RSA or ECDSA.
"""

# pip install PyJWT

import jwt
from datetime import datetime, timedelta

SECRET_KEY_APP = "25a2aaaed449c7d3125c9fd6d3131e109f6531f35db1c519b4c1ee6a3352dc85"



def generate_jwt(payload, expiration_in_minutes=60):
    """ GENERATE JWT  """
    expiration = datetime.utcnow() + timedelta(minutes=expiration_in_minutes)
    payload['exp'] = expiration
    return jwt.encode(payload=payload, key=SECRET_KEY_APP, algorithm="HS256")

def verify_jwt(token: str):
    """ VERIFY and DECODE JWT """
    try:
        return jwt.decode(jwt=token, key=SECRET_KEY_APP, algorithms="HS256")
    except jwt.ExpiredSignatureError:
        return "TOKEN EXPIRED"
    except jwt.InvalidTokenError:
        return "INVALID TOKEN"
    
# usage
payload = {"user_id": 1, "name": "jaka prima maulana"}
jwt_token = generate_jwt(payload=payload)
print("GENERATED_TOKEN", jwt_token)


decode_payload = verify_jwt(jwt_token)
print("DECODE PAYLOAD", decode_payload)
