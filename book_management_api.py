from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

books=[]

class Book(BaseModel):
    id:int
    title:str
    author:str
    price:int
    available:bool
    category:str
    
# create books
@app.post("/books")
def create_book(book:Book):
 
    for existing_book in books:
        if existing_book.id == book.id:
            return{
                "Error":"Book ID already exists"
            }
    books.append(book)

    return{
        "message":"Book added successsfully",
         "data":book

     }  



@app.get("/books")
def get_books(
     search: str = None,
    author: str = None,
    category: str = None,
    available: bool = None,
    min_price: int = None,
    max_price: int = None
):

    result = books.copy()

    if search:
        result =[
            book for book in result
            if search.lower() in book.title.lower()
        ]


    if author:
        result =[
            book for book in result
            if book.author.lower() == author.lower() 
        ]


    if category:
        result =[
            book for book in result
            if book.category.lower() == category.lower() 
        ]

    if available is not None:
        result =[
            book for book in result
            if book.available == available 
        ]


    if min_price is not None:

        result = [
            book for book in result
            if book.price >= min_price
        ]

        
    if max_price is not None:
        result = [
            book for book in result
            if book.price <= max_price
        ]

    return result


        

        


#read one book\
@app.get("/books/{book_id}")
def get_book(book_id:int):
    for book in books:
        if book.id == book_id:
            return book

    return{
        "error":"book is not found"
    }    


# UPDATE ONE BOOK
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):

    for index, book in enumerate(books):

        if book_id == book.id:

            updated_book.id = book_id

            books[index] = updated_book
  

            return {
                "message": "Book updated successfully",
                "data": updated_book
            }

    return {
        "error": "Book is not found"
    }


@app.delete("/books/{book_id}")
def delete_book(book_id:int):
    for index,book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return{
                "message":"Book deleted"
            }
    return{
            "error":"Book not found"
        }
