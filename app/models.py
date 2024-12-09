from typing import Dict, Any

class Book:
    books = {}
    book_id_counter = 1

    @classmethod
    def create(cls, title: str, author: str):
        book_id = cls.book_id_counter
        cls.books[book_id] = {"id": book_id, "title": title, "author": author}
        cls.book_id_counter += 1
        return cls.books[book_id]

    @classmethod
    def read(cls, book_id: int):
        return cls.books.get(book_id)

    @classmethod
    def update(cls, book_id: int, data: Dict[str, Any]):
        if book_id in cls.books:
            cls.books[book_id].update(data)
            return cls.books[book_id]
        return None

    @classmethod
    def delete(cls, book_id: int):
        return cls.books.pop(book_id, None)

    @classmethod
    def search(cls, query: str):
        return [
            book for book in cls.books.values()
            if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()
        ]

class Member:
    # Similar to Book
    pass

def init_db():
    # Initialize with some sample data if needed
    pass
