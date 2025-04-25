from fastapi import FastAPI,Query,Path
from dotenv import load_dotenv
import os
import uvicorn
from typing import List, Tuple, Dict   
from functools import reduce
from backend.routes import practice_route,book_route
 
load_dotenv()  # Loads variables from .env

app = FastAPI()

app.include_router(practice_route.router)
app.include_router(book_route.router)


@app.get("/")
def home():
    def prac1(a: int , b: float)->List :
        """
        this function is just an start
        """
        return [a-b,a,a+b]
    
    return {"message": "We are starting with Fast API", "env": os.getenv("APP_ENV"), "function with type hint" : prac1  (1,2)}

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


if __name__ == '__main__':      
    # app.run(debug=False, port=5000)
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)   