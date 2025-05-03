"""
Models Are Used For SQLAlchemy which is an ORM and used for DB connection compared to
pydantic which is more used for validations. 

"""

from pydantic import BaseModel,Field,EmailStr
from typing import List,  Dict, Tuple
class User(BaseModel):
    name: str=Field(None,title= "Full name of user",min_length=2,max_length=10)
    email: EmailStr
    phones: str
    password: str
    role:str
    is_active:bool
    