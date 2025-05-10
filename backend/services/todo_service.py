from fastapi import HTTPException

from models import Todo
from schemas.todo_request import   TodoRequest

from sqlalchemy.orm import Session



def get_all_todos(db):
    return db.query(Todo).all()

def get_current_user_todos(user,db):
    return db.query(Todo).filter(Todo.user_id==user.get("payload")["id"]).all()


def get_todo_by_id(db:Session,todo_id):
    print(db.get(Todo,todo_id))
    return db.get(Todo,todo_id)

def insert_into_todo(user,db,todo_data:TodoRequest):
    if  not user :
        raise HTTPException(status_code=401, detail="User is not logged in.")
    new_todo_model = Todo(**todo_data.model_dump(),user_id=user.get("payload")["id"])
    db.add(new_todo_model)
    db.commit()
    db.refresh(new_todo_model)
    return new_todo_model
def update_todo_by_id(user,db,todo_id,updated_todo):
    if  not user :
        raise HTTPException(status_code=401, detail="User is not logged in.")
    print(user.get("role").casefold())
    if user.get("role").casefold()!="admin":
        raise HTTPException(status_code=401, detail="Only admin can access.")

    saved_todo=db.query(Todo).filter(Todo.id==todo_id).first()
    if not saved_todo:
        raise HTTPException(status_code=401, detail="Unable to found todo.")
    for key, value in updated_todo.model_dump().items():
        if key not in ["id","user_id"]:
            setattr(saved_todo, key, value)
    db.commit()
    db.refresh(saved_todo)
    return saved_todo

