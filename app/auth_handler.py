import time 
from typing import Dict 
import jwt 
from decouple import config 

JWT_SECRET = config("JWT_SECRET") 
JWT_ALGORITHM = config("JWT_ALGORITHM") 
JWT_EXP = config("JWT_EXP", cast=int)

def token_response(token: str) -> Dict[str, str]: 
    return {"access_token": token}
