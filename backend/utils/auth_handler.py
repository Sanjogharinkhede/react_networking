
from datetime import timedelta,datetime, timezone
import os
from dotenv import load_dotenv
from jose import jwt

load_dotenv()

def create_access_token(username:str, user_id:int, expire_delta:timedelta):
    encode={
        'sub':username,
        'id':user_id,
        'exp':datetime.now(timezone.utc)+expire_delta
    }
    
    return jwt.encode(encode,os.getenv("SECRET_KEY"),algorithm=os.getenv("ALGORITHM")) 