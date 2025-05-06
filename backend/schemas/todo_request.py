from datetime import date, datetime
from pydantic import BaseModel


class TodoRequest(BaseModel):
    title: str
    desc: str
    priority: int
    completed: bool
    start_date: date
    end_date: datetime

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Finish FastAPI Project",
                "desc": "Implement the remaining CRUD operations and test endpoints.",
                "priority": 5,
                "completed": False,
                "start_date": "2025-04-29",
                "end_date": "2025-05-01T18:00:00"
            }
        }
    }
