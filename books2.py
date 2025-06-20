from typing import Optional
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
app = FastAPI()


class Book:
    id: int
    title:str  
    author: str
    description:str
    rating: float
    published_date :int

    def __init__(self, id,title, author, description, rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date 


class BookRequest(BaseModel):
    id : Optional[int] = Field(description= "ID is not needed on create",default=None) 
    title : str = Field(min_length=3)
    author : str = Field(min_length=1)
    description : str = Field(min_length=1, max_length=100)
    rating : int = Field(gt=0, lt=6)
    published_date : int = Field(description= "Fromat:YYYY", gt =1999, lt = 2031 ) 

    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A new book",
                "author":"codingwithroby",
                "description":"a new description of a book",
                "rating":5,
                "published_date": 2029
            }
        }
    }



BOOKS = [
    Book(1,"Computer Science Pro","Codingwithroby","A very nice book!",5,2000),
    Book(2,"Be Fast with Fastapi","Codingwithroby","A great book!",5,2000),
    Book(3,"Master Endpoints","Codingwithroby","A awesome book!",5,2002),
    Book(4,"HP1","Author 1","Book Description",2,2003),
    Book(5,"HP2","Author 2","Book Description",3,2004),
    Book(6,"HP3","Author 3","Book Description",1,2005)

]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/book/{book_id}")
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book 

@app.get("/books/publish/")
async def get_book_by_published_date(published_date:int = Query(gt=1999,lt=2031)):
    book_published = []
    for book in BOOKS:
        if book.published_date == published_date:
            book_published.append(book)
    return book_published        


@app.get("/books/")
async def read_book_by_rating(book_rating:int = Query(gt=0,lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)

    return books_to_return





@app.post("/create-book")
async def create_book(book_request : BookRequest):
    # print(book_request.id)
    # print(type(book_request))
    new_book = Book(**book_request.model_dump())
    # print(type(new_book))
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):

    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id +1
   
   
    # if len(BOOKS) > 0:
    #     book.id = BOOKS[-1].id +1
    # else:
    #     book.id = 1
    
    return book


@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete("/books/{book_id}")
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break