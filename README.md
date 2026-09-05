# fastapi-book-management-api
A beginner-friendly Book Management REST API built with FastAPI and Pydantic, featuring CRUD operations, search, and filtering.
# FastAPI Book Management API

A simple Book Management REST API built using **FastAPI** and **Pydantic**.

This project is created for learning and practicing API development with FastAPI.

## Features

* Create a book
* Get all books
* Get a single book by ID
* Update a book
* Delete a book
* Search books by title
* Filter books by author
* Filter books by category
* Filter books by availability
* Filter books by minimum price
* Filter books by maximum price

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
fastapi-book-management-api/
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
```

Go into the project directory:

```bash
cd fastapi-book-management-api
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically provides interactive API documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## API Endpoints

### Create a Book

```http
POST /books
```

Example request:

```json
{
    "id": 1,
    "title": "Python Basics",
    "author": "John Smith",
    "price": 500,
    "available": true,
    "category": "Programming"
}
```

### Get All Books

```http
GET /books
```

### Search Books

```http
GET /books?search=python
```

### Filter by Author

```http
GET /books?author=John Smith
```

### Filter by Category

```http
GET /books?category=Programming
```

### Filter by Availability

```http
GET /books?available=true
```

### Filter by Price

```http
GET /books?min_price=300&max_price=800
```

### Get One Book

```http
GET /books/{book_id}
```

Example:

```http
GET /books/1
```

### Update a Book

```http
PUT /books/{book_id}
```

Example:

```http
PUT /books/1
```

Request body:

```json
{
    "id": 1,
    "title": "Advanced Python",
    "author": "John Smith",
    "price": 700,
    "available": true,
    "category": "Programming"
}
```

### Delete a Book

```http
DELETE /books/{book_id}
```

Example:

```http
DELETE /books/1
```

## Important Note

This project currently uses an in-memory Python list to store books:

```python
books = []
```

Therefore, all data will be lost when the FastAPI server is restarted.

A future version can use a database such as MySQL or PostgreSQL.

## Future Improvements

* Add MySQL/PostgreSQL database
* Add SQLAlchemy
* Add proper HTTP status codes
* Add pagination
* Add better error handling
* Add authentication
* Add unit tests
* Add Docker support

## Learning Goals

This project demonstrates the basic concepts of building a REST API using FastAPI, including:

* Pydantic models
* HTTP methods
* Path parameters
* Query parameters
* CRUD operations
* Searching
* Filtering
* API documentation

