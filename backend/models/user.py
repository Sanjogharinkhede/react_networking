"""
Models Are Used For SQLAlchemy which is an ORM and used for DB connection compared to
pydantic which is more used for validations. 

"""
from configs.db import Base
from sqlalchemy import Column, Integer,String,Boolean,Date,DateTime
from datetime import datetime
from sqlalchemy.sql import func

class User(Base):
    __tablename__= "users"
    
    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    name=Column(String,index=True)
    email=Column(String,unique=True,index=True)
    phones=Column(String,index=True)
    password=Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) #SQL server automatically sets it to current time.
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) #Updates automatically when the record changes.
    
    
    