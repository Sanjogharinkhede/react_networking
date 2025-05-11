from configs.db import Base
from sqlalchemy import Column, ForeignKey, Integer,String,Boolean,Date,DateTime
from datetime import datetime
from sqlalchemy.sql import func

class Todo(Base):
    __tablename__= "todos"
    
    id=Column(Integer, primary_key=True,autoincrement=True,index=True)
    title=Column(String(255))
    desc=Column(String(255))
    priority=Column(Integer)
    completed=Column(Boolean,default=False)
    start_date=Column(Date,default=datetime.utcnow)
    end_date=Column(DateTime,default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) #SQL server automatically sets it to current time.
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) #Updates automatically when the record changes.
    
    