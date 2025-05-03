from fastapi import APIRouter,Body,Path,Query,HTTPException
from starlette import status
from  services import todo_service

from typing import Annotated
from fastapi import Depends
from configs.db import get_db
from sqlalchemy.orm import Session
from schemas import Todo as TodoRequest


router= APIRouter(prefix="/todo",tags=["Todo"])
db_depends=Annotated[Session,Depends(get_db)]

@router.get("/",status_code=status.HTTP_200_OK)
async def  get_all_task(db:db_depends):
    return todo_service.get_all_todos(db)
@router.get("/{id}",status_code=status.HTTP_200_OK)
async def get_task_by_id(db:db_depends,id:int=Path(gt=0)):
    return todo_service.get_todo_by_id(db,id)

@router.post("/add",status_code=status.HTTP_201_CREATED)
async def add_a_task(db:db_depends,todo:TodoRequest=Body()):
    return todo_service.insert_into_todo(db,todo)