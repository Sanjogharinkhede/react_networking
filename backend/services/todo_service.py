from fastapi import HTTPException

from models import Todo
from schemas.todo_request import   TodoRequest

from sqlalchemy.orm import Session



def get_all_todos(db):
    return db.query(Todo).all()


def get_todo_by_id(db:Session,id):
    print(db.get(Todo,id))
    return db.get(Todo,id)

def insert_into_todo(user,db,todo_data:TodoRequest):
    if  not user :
        raise HTTPException(status_code=401, detail="User is not logged in.")
    new_todo_model = Todo(**todo_data.model_dump(),user_id=user.get("id"))
    db.add(new_todo_model)
    db.commit()
    db.refresh(new_todo_model)
    