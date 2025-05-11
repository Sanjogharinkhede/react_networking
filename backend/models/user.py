"""
Models Are Used For SQLAlchemy which is an ORM and used for DB connection compared to
pydantic which is more used for validations. 

"""
from configs.db import Base
from sqlalchemy import Column, Integer,String,Boolean,Date,DateTime,Enum
from sqlalchemy.sql import func
from datetime import datetime

class User(Base):
    __tablename__= "users"
    
    id=Column(Integer,primary_key=True,autoincrement=True,index=True)
    name=Column(String(255),index=True)
    email=Column(String(255),unique=True,index=True)
    phones=Column(String(255),index=True)
    password=Column(String(255))
    dob=Column(Date,default=datetime.utcnow)
    role=Column(String(255),index=True)
    is_active=Column(Boolean,default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) #SQL server automatically sets it to current time.
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) #Updates automatically when the record changes.
    
    
    