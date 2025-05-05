
from datetime import timedelta,datetime, timezone
import os
from typing import Annotated

from dotenv import load_dotenv
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

load_dotenv()
oauth2_bearer=OAuth2PasswordBearer(tokenUrl="auth/login")

def create_access_token(username:str, user_id:int, expire_delta:timedelta):
    encode={
        'sub':username,
        'id':user_id,
        'exp':datetime.now(timezone.utc)+expire_delta
    }
    
    return jwt.encode(encode,os.getenv("SECRET_KEY"),algorithm=os.getenv("ALGORITHM"))

def get_user_with_jwt(token:Annotated[str,Depends(oauth2_bearer)]):
    try:
        payload =jwt.decode(token,os.getenv("SECRET_KEY"),algorithms=[os.getenv("ALGORITHM")])
        email :str=payload.get('sub')
        user_id:int =payload.get('id')
        if not email or not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="No User found")
        return  {'email':email,"payload":payload}
    except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,detail="JWT ERROR ")

