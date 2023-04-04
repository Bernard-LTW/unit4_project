from jose import JWTError, jwt
import os
import dotenv
import datetime

dotenv.load_dotenv()
token_encryption_key = os.getenv("TOKEN_ENCRYPTION_KEY")

def create_token(username, token_duration): #token = encoded(username, datetime) token_duration in minutes
    token  = jwt.encode({'username': username, 'datetime': datetime.datetime.now() + datetime.timedelta(minutes=token_duration)}, token_encryption_key, algorithm='HS256')

def check_token(token): #check if token is valid and not expired
    try:
        decoded_token = jwt.decode(token, token_encryption_key, algorithms=['HS256'])
        if decoded_token['datetime'] < datetime.datetime.now():
            return False
        else:
            return True
    except:
        return False


