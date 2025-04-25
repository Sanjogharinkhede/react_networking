from FastAPI import APIRouter
from models.book import Book
router= APIRouter(prefix="/books",tags=["books", "api"])

all_books=[
    Book(1,"book_1",["auth1","auth11"],3,99,{"publication":"mcgraw","year":2019}),
    Book(2,"book_2",["auth2","auth21"],2,299,{"publication":"tc","year":2009}),
    Book(3,"book_3",["auth3","auth31"],5,999,{"publication":"lal","year":2011}),
    Book(4,"book_4",["auth4","auth41"],1,799,{"publication":"poll","year":2013})
]

@router.get("/")
async def get_all_books():
    return all_books
