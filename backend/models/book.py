from typing import List, Dict
# from pydantic import BaseModel

class Book():
    id: int
    title: str
    authors: List[str]
    rating: int
    price: float
    metadata: Dict[str, str]


    def __init__(
        self,
        id: int,
        title: str,
        authors: List[str],
        rating: int,
        price: float,
        metadata: Dict[str, str],
    ):

        self.id = id
        self.title = title
        self.authors = authors
        self.rating = rating
        self.price = price
        self.metadata = metadata
