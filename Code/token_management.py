from jose import JWTError, jwt
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()
token_encryption_key = os.getenv("TOKEN_ENCRYPTION_KEY")

def create_token(username, token_duration): #token = encoded(username, datetime) token_duration in minutes
    unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
    ttl = token_duration * 60 + unix_timestamp
    token  = jwt.encode({'username': username, 'datetime': unix_timestamp}, token_encryption_key, algorithm='HS256')
    return token

def get_username_from_token(token): #get username from token
    print(token)
    decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
    return decoded_token['username']

def check_token(token): #check if token is valid and not expired
    try:
        decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
        unix_timestamp = (datetime.now() - datetime(1970, 1, 1)).total_seconds()
        if decoded_token['datetime'] < unix_timestamp:
            return False
        else:
            return True
    except:
        return False

