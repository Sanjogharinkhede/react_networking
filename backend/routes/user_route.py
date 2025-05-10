from typing import Annotated

from fastapi import APIRouter, Body, Depends
from fastapi.params import Query
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from configs.db import get_db
from routes.todo_route import user_dependency
from schemas import Token, User as UserRequest
from services import user_service
from utils.auth_handler import get_current_user_with_jwt

router = APIRouter(prefix="/auth",tags=["User Authentication"])
db_depends=Annotated[Session,Depends(get_db)]
user_dependency=Annotated[dict,Depends(get_current_user_with_jwt)]

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_new_user(db:db_depends,user:UserRequest = Body()):
        return user_service.create_user(db,user)
        
@router.post("/login",status_code=status.HTTP_200_OK,response_model=Token)
async def login_for_access_token(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:db_depends):
        return user_service.get_token(form_data,db)

@router.get("/profile",status_code=status.HTTP_200_OK)
async def get_user_details(user:user_dependency,db:db_depends):
        return {"user_by_jwt":user, "user_model":user_service.get_user_details(user,db)}


@router.patch("/change_password",status_code=status.HTTP_204_NO_CONTENT)
async def change_password(db:db_depends,email:str=Query(),old_password:str=Query(),new_password:str=Query()):
        return user_service.change_password(db,email,old_password,new_password)
