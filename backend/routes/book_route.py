from fastapi import APIRouter,Body,Path,Query,HTTPException
from models.book import Book
from schemas.book_schema import Book as BookModel
from starlette import status
router= APIRouter(prefix="/books",tags=["books"])

all_books=[
    Book(1,"book_1",["auth1","auth11"],3,99,{"publication":"mcgraw","year":"2019"}),
    Book(2,"book_2",["auth2","auth21"],2,299,{"publication":"tc","year":"2009"}),
    Book(3,"book_3",["auth3","auth31"],5,999,{"publication":"lal","year":"2011"}),
    Book(4,"book_4",["auth4","auth41"],1,799,{"publication":"poll","year":"2013"}),
    Book(5,"book_5",["auth34","auth31"],5,1999,{"publication":"pal","year":"2021"}),
]

@router.get("/",status_code=status.HTTP_200_OK)
async def get_all_books():
    return all_books

@router.get("/author/{author_name}",status_code=status.HTTP_200_OK)
async def get_author_books(author_name:str):
    my_book=list(filter(lambda book : author_name.casefold() in book.authors,all_books))
    return {"total_books":len(my_book),"books":my_book}

@router.get("/{book_name}",status_code=status.HTTP_200_OK)
async def get_book_by_name(book_name:str):
    my_book=list(filter(lambda book : book.title.casefold()==book_name.casefold() ,all_books))
    if len(my_book)>0:
        return {"total_books":len(my_book),"books":my_book}
    else:
        raise HTTPException(status_code=404,detail="There are no books available")

@router.post("/create",status_code=status.HTTP_201_CREATED)
async def create_a_book(book:BookModel=Body()):
    all_books.append(book)
    return all_books

@router.put("/update",status_code=status.HTTP_204_NO_CONTENT)
async def update_book_by_id(id : int =Query(default=None,gt=0) ,book:BookModel=None):
    for i in range(len(all_books)):
        if all_books[i].id==id:
            book.id=id
            all_books[i]=book
            return all_books
    return {"msg":"id not found"}           
            
@router.delete("/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book_by_id(id:int=Path(gt=0)):
    for i in range(len(all_books)):
        if all_books[i].id==id:
            all_books.pop(i)
            return all_books
    return {"msg":"id not found"}