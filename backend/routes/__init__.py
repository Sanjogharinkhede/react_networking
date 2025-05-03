from routes.book_route import router as book_router
from routes.todo_route import router as todo_router
from routes.practice_route import router as practice_router
from routes.gemini_route import router as gemini_router
from routes.user_route import router as auth_router

all_routes = [
    book_router,
    todo_router,
    practice_router,
    gemini_router,
    auth_router
]