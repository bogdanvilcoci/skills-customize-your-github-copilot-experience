from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Book Library API")


class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    publication_year: int = Field(ge=0)


class Book(BookCreate):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J. R. R. Tolkien", publication_year=1937),
    2: Book(id=2, title="A Wrinkle in Time", author="Madeleine L'Engle", publication_year=1962),
}


@app.get("/")
def read_root():
    return {"message": "Welcome to the Book Library API"}


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return all books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Return the requested book or raise an HTTP 404 error.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookCreate):
    # TODO: Assign a new ID, save the book, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def replace_book(book_id: int, book_data: BookCreate):
    # TODO: Replace the book's details, keeping its ID, or raise HTTP 404.
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    # TODO: Delete the book or raise HTTP 404.
    pass
