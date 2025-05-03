from fastapi import APIRouter,Body, Depends,HTTPException
from configs.db import get_db
from schemas import User as UserRequest
from services import user_service
from starlette import status
from sqlalchemy.orm import Session
from typing import Annotated

router = APIRouter(prefix="/auth",tags=["User Authentication"])
db_depends=Annotated[Session,Depends(get_db)]


@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_new_user(db:db_depends,user:UserRequest = Body()):
        return user_service.create_user(db,user)
        