from fastapi import APIRouter,Body
from schemas import User as UserRequest

router = APIRouter(prefix="/auth",tags=["User Authentication"])

@router.post("/")
def create_new_user(user:UserRequest = Body()):
    pass