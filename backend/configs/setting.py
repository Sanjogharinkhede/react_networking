""""
Will User Later for Env Related Secrets
"""
from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()


"""

MONGO_URI=mongodb://localhost:27017/networkingdb


APP_ENV="Development"

SECRET_KEY='e5f08cf5bd18c496773ba5e8d3ac74292a810a0aeb54a6e8065df48c6e7d0a23'
ALGORITHM='HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

GEMINI_KEY=AIzaSyChn5MaunVyrExauHPstceTwaxtOtdTI14


SQLALCHEMY_DATABASE_URL_SQLITE='sqlite:///./todos_app.db'
SQLALCHEMY_DATABASE_URL_POSTGRES='postgresql://postgres:Sanjog%40123@localhost:5432/sanjog_db'
SQLALCHEMY_DATABASE_URL_MYSQL='mysql+pymysql://root:123456@localhost:3306/sanjog_may_db'

HOST=0.0.0.0
PORT=5000

DB_USER=postgres
DB_PASSWORD=Sanjog@123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sanjog_db


"""