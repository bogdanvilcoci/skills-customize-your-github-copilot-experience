# 📘 Assignment: Building REST APIs with FastAPI

**Difficulty:** Intermediate

## 🎯 Objective

Build a REST API for managing a small book library. Using FastAPI and Pydantic, you will create endpoints to list, add, update, and remove books, and practice how an API validates requests and responds to clients.

## 📚 Learning Objectives

By completing this assignment, you will be able to:

- Define API endpoints and HTTP methods with FastAPI.
- Describe and validate request and response data with Pydantic models.
- Return appropriate HTTP status codes and handle missing resources.
- Run and test an API locally using its interactive documentation.

## ✅ Before You Begin

- Be comfortable with Python functions, dictionaries, and type annotations.
- Install Python 3.10 or later.
- Install the required packages with `python -m pip install fastapi uvicorn`.
- Open [`main.py`](./main.py), which contains the initial data and starter structure.

## 📝 Tasks

### 🛠️ Review the API and Book Models

#### Description
Use the FastAPI application and Pydantic schemas in the starter code as the foundation for your endpoints. Review how the input and response models describe a book and validate client data.

#### Requirements
Completed program should:

- Use the provided FastAPI application and its descriptive title.
- Accept a title, author, and publication year in book requests.
- Include an integer ID in book responses.
- Reject empty titles or authors and negative publication years using the provided Pydantic field constraints.

### 🛠️ Add Read Endpoints

#### Description
Let clients retrieve the books in the library or look up one book by its ID.

#### Requirements
Completed program should:

- Provide `GET /books` to return all books.
- Provide `GET /books/{book_id}` to return the matching book.
- Return an HTTP 404 response when the requested book ID does not exist.
- Use response models so the returned data follows the book model.

### 🛠️ Implement Create, Update, and Delete

#### Description
Add the remaining operations so clients can manage the library. Keep the starter data in memory; changes do not need to persist after the server stops.

#### Requirements
Completed program should:

- Provide `POST /books` to add a validated book, assign it a unique ID, and return HTTP 201.
- Provide `PUT /books/{book_id}` to replace an existing book's details while keeping its ID.
- Return HTTP 404 when an update or delete targets a book that does not exist.
- Provide `DELETE /books/{book_id}` and return HTTP 204 when the book is deleted.

### 🛠️ Run and Test the API

#### Description
Start your API and use FastAPI's interactive documentation to try each operation and check both successful and unsuccessful requests.

#### Requirements
Completed program should:

- Start with `python -m uvicorn main:app --reload` from the assignment folder.
- Make the interactive API documentation available at `http://127.0.0.1:8000/docs`.
- Demonstrate listing, retrieving, creating, updating, and deleting books.
- Demonstrate a validation error and a 404 response for a missing book.

Build and test one endpoint at a time. Remember that this assignment uses in-memory data, so restarting the server restores the original sample books.
