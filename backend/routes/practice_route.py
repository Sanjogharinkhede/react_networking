from schemas.user import User
from fastapi import APIRouter, HTTPException,Body,Path,Query,responses,UploadFile, File
import aiofiles



router = APIRouter(prefix="/myPractice", tags=["MyPractice"])





@router.post("/")
async def create(user:User) -> User:
    return user




@router.post("/prac/")
async def create_user(name:str = Body(...,alias="One Alias is used",max_length=50)) -> User:
    return name





"""
This func is used to demostrate path() and query() and body() from fastapi
and 
we can also use field in model to define The User model and validate user data.
    """
@router.post("/prac3InOne/{path_var}")
async def create_user_prac(path_var:str = Path(...,min_length=3,description="some Desc"), 
                           query_param:int =Query(None, ge=18),
                           req_body : dict=Body(...,max_length=2),user:User=None):
    return {"a":path_var,"b":query_param,"c":req_body,"d":user}




@router.get("/htmlResp")
async def create_html_resp():
    return  responses.HTMLResponse(content="<h4>ABC<h4>")




@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = f"../frontend/public/assets/uploads/{file.filename}"  
    async with aiofiles.open(file_location, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)
    
    return {"info": f"File  '{file.filename}' saved at '{file_location}'"}