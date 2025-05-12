from alembic.util import status
from fastapi import FastAPI
from dotenv import load_dotenv
import os
import uvicorn
from typing import List, Tuple, Dict   
from functools import reduce
from routes import all_routes
import models
from configs.db import engine
from starlette import status
load_dotenv()  # Loads variables from .env

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

for route in all_routes:
    app.include_router(route)


@app.get("/",status_code=status.HTTP_200_OK)
def home():
    def prac1(a: int , b: float)->List :
        """
        this function is just an start
        """
        return [a-b,a,a+b]
    
    return {"status":"True","message": "We are starting with Fast API", "env": os.getenv("APP_ENV"), "function with type hint" : prac1  (1,2)}


if __name__ == '__main__':      
    # app.run(debug=False, port=5000)
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("app:app", host=host, port=port, reload=True)
    # app = FastAPI(openapi_url=None, docs_url=None, redoc_url=None)











# -----------------------------------------------------------------------------------------------------#

# @app.get("/{name}/{age}")
# async def prac2(name : str, age:int)->str :
#     """
#     path variable needed an right type or an error as response. 
#     """
#     return f"Your name is {name} and you are {age} year old."

# @app.get("/query")
# async def prac3(works : List[str]= Query(None), salary:float=0)->str :
#     """
#     path variable needed an right type or an error as response. 
#     """
#     return f"Your works are {reduce(lambda x,y: f"{x}, {y}" ,works)} and you're salary is {salary}k."

# @app.get("/query/{topic}")
# def get_content(
#     topic: str = Path(...,min_length=3,max_length=10),
#     level: str = Query("beginner"),
#     age: int = Query(None, ge=18,le=60,)
# ):
#     return {"topic": topic, "level": level,"age":age}

# -----------------------------------------------------------------------------------------------------#


