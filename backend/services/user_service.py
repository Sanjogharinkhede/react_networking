from datetime import timedelta

from starlette import status

from schemas import User as UserRequest
from models import User 

from sqlalchemy.orm import Session
from typing import Annotated, Any
from fastapi import Depends ,HTTPException
from configs.db import get_db
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from utils.auth_handler import create_access_token 


bcrypt_context=CryptContext(schemes=['bcrypt'],deprecated='auto')
def create_user(db,user:UserRequest):
    try:
        user_model= User(**user.model_dump())
        user_model.password=bcrypt_context.hash(user_model.password)
        db.add(user_model)
        db.commit()
        db.refresh(user_model)
        return {"status":True,"msg":"User Added Successfully","user":user_model}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=e)
    
    
def get_token(form_data,db):
    user:User=authenticate_user(db,form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="No user found with given credentials.")
    token=create_access_token(user.email,user.id,user.role,timedelta(minutes=30))
    return {"status":True, "form_data":form_data,"access_token":token,"token_type":"bearer"}

def authenticate_user(db,email, password)-> User| None:
    user =db.query(User).filter(email==User.email).first()
    if not user or not bcrypt_context.verify(password,user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Password not matched for user")
    return user