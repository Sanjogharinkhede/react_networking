from .book_route import router as book_router
from .todo_route import router as todo_router
from .practice_route import router as practice_router
from .gemini_route import router as gemini_router

all_routes = [
    book_router,
    todo_router,
    practice_router,
    gemini_router
]