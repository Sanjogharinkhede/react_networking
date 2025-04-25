from typing import List, Dict


class Book():
    id: int
    title: str
    authors: List[str]
    rating: int
    price: float
    metadata: Dict[str, any]


def __init__(
    self,
    id: int,
    title: str,
    authors: List[str],
    rating: int,
    price: float,
    metadata: Dict[str, any],
):

    self.id = id
    self.title = title
    self.authors = authors
    self.rating = rating
    self.price = price
    self.metadata = metadata
