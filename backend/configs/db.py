"""
Will be used for connection to db.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

# ---------------------------------
#for sqlite  we use connect_args check thread as sqlite is single thread only and you needed to tell that
# it request can come from multiple thread



# engine =create_engine(os.getenv("SQLALCHEMY_DATABASE_URL"),connect_args={'check_same_thread':False})
# ---------------------------------


# ---------------------------------
engine =create_engine(os.getenv("SQLALCHEMY_DATABASE_URL_POSTGRES"))
# ---------------------------------

# ---------------------------------
engine =create_engine(os.getenv("SQLALCHEMY_DATABASE_URL_MYSQL"))
# ---------------------------------



SessionLocal =sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base= declarative_base()


def get_db():
    db= SessionLocal()
    try:
        yield db
    finally:
        db.close()