from jose import JWTError, jwt
import os
import dotenv


dotenv.load_dotenv()
token_encryption_key = os.getenv("TOKEN_ENCRYPTION_KEY")
