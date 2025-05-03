from datetime import date, datetime
from configs.db import Base
from sqlalchemy.sql import func
from pydantic import BaseModel,Field
from typing import Optional


class Todo(BaseModel):
    
    id:Optional[int]=Field(default=None, description="ID not needed on create")
    title:str
    desc:str
    priority:int
    completed:bool
    start_date:date
    end_date:datetime
    user_id:int
    created_at :datetime
    updated_at:datetime
     #it will be an example shown in swagger doc for user
    model_config={
        "json_schema_extra":{
            "example":{
  "title": "Finish FastAPI Project",
  "desc": "Implement the remaining CRUD operations and test endpoints.",
  "priority": 1,
  "completed": False,
  "start_date": "2025-04-29",
  "end_date": "2025-05-01T18:00:00",
  "user_id":1,
  "created_at": "2025-04-29T12:00:00",
  "updated_at": "2025-04-29T14:30:00"
}

        }
    }