import jwt
from jwt.algorithms import get_default_algorithms

# JWT token received from the client
jwt_token = 'your_jwt_token_here'

# Secret key used for signing the JWT token
secret_key = 'your_secret_key_here'

# Function to verify JWT token
def verify_jwt_token(token):
    # Get default algorithms
    algorithms = get_default_algorithms()

    try:
        # Decode the token without verifying the algorithm
        decoded_payload = jwt.decode(token, options={"verify_signature": False})
        
        # Get the algorithm from the decoded header
        header_algorithm = decoded_payload.get('alg')

        # Get the algorithm from the backend configuration (for example, from a settings file)
        backend_algorithm = 'HS256'  # Example value, replace with your actual backend algorithm
        
        # Verify that the algorithm from the header matches the backend algorithm
        if header_algorithm == backend_algorithm:
            # Verify the token with the specified algorithm and secret key
            decoded_payload = jwt.decode(token, secret_key, algorithms=[backend_algorithm])
            return decoded_payload
        else:
            # Algorithm mismatch, token is invalid
            raise jwt.InvalidTokenError("Invalid algorithm")
    except jwt.ExpiredSignatureError:
        # Token has expired
        raise jwt.ExpiredSignatureError("Token has expired")
    except jwt.InvalidTokenError:
        # Invalid token
        raise jwt.InvalidTokenError("Invalid token")

# Verify the JWT token
try:
    payload = verify_jwt_token(jwt_token)
    print("Token verified successfully. Payload:", payload)
except jwt.ExpiredSignatureError as e:
    print("Error:", e)
except jwt.InvalidTokenError as e:
    print("Error:", e)
