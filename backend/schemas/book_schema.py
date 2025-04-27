from typing import List, Dict,Optional
import datetime
from pydantic import BaseModel,Field

class Book(BaseModel):
    
    id: Optional[int]=Field(default=None, description="ID not needed on create") #to make this field optional for user so that it can bee changed by user only
    
    title: str=Field(min_length=3)
    authors: List[str]=Field(min_length=1)
    rating: int
    price: float
    metadata: Dict[str, str]
    
    
    #it will be an example shown in swagger doc for user
    model_config={
        "json_schema_extra":{
            "example":{
                "title": "New book",
                "authors": ["auth1","auth2"],
                "rating": 5,
                "price": 99.99,
                "metadata": {"last_update": datetime.datetime.now().strftime("%A, %b %d,%Y "),"year": f"{datetime.datetime.now().year}"}
            }
        }
    }