from models import Todo
from schemas import Todo as TodoSchema

from sqlalchemy.orm import Session



def get_all_todos(db):
    return db.query(Todo).all()


def get_todo_by_id(db:Session,id):
    print(db.get(Todo,id))
    return db.get(Todo,id)

def insert_into_todo(db,todo_data:TodoSchema):
    new_todo_model = Todo(**todo_data.model_dump())
    db.add(new_todo_model)
    db.commit()
    db.refresh(new_todo_model)
    