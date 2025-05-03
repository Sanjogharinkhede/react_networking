from schemas import User as UserRequest
from models import User 

from sqlalchemy.orm import Session
from typing import Annotated
from fastapi import Depends ,HTTPException
from configs.db import get_db

def create_user(db,user:UserRequest):
    try:
        user_model= User(**user.model_dump())
        db.add(user_model)
        db.commit()
        db.refresh(user_model)
        return {"status":True,"msg":"User Added Successfully"}
    except Exception as e:
        raise Exception("Something went wrong")
    
    