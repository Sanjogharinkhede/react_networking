from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env

app = FastAPI()

@app.get("/")
def home():
    return {"message": "We are starting with Fast API", "env": os.getenv("APP_ENV")}

if __name__ == '__main__':      
    app.run(debug=False, port=5000)