from .book_route import router as book_router
from .todo_route import router as todo_router
from .practice_route import router as practice_router
from .gemini_route import router as gemini_router
from .auth_route import router as auth_router

all_routes = [
    book_router,
    todo_router,
    practice_router,
    gemini_router,
    auth_router
]