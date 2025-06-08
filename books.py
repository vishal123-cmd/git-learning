from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"title":"Title one", "author":"Author One","Category": "Science"},
    {"title":"Title two", "author":"Author two","Category": "Science"},
    {"title":"Title three", "author":"Author three","Category": "history"},
    {"title":"Title Four", "author":"Author four","Category": "math"},
    {"title":"Title Five", "author":"Author five","Category": "math"},
    {"title":"Title Six", "author":"Author two","Category": "math"}
]


@app.get("/books")
async def read_all_books():
    return BOOKS

# Path parameters
@app.get("/books/{book_title}")
async def read_all_books(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


# path parameters with type hinting
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}


# @app.get("/books/")
# async def read_category_by_query(category: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('category').casefold() == category.casefold():
#             books_to_return.append(book)
        
#     return books_to_return

# @app.get("/books/")
# async def read_category_by_query(category: str):
#     books_to_return = []
#     for book in BOOKS:
#         if book.get('category').casefold() == category.casefold():
#                     books_to_return.append(book)
#     return books_to_return


# Query parameters  
@app.get("/books/")
async def read_category_by_query(Category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('Category').casefold() == Category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/")
async def read_root():
    return "Hello, World! This is the root endpoint." 

# Path parameters and Query parameters combined
@app.get("/books/{book_author}/")
async def read_category_by_query(book_author : str, Category:str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get("Category").casefold() == Category.casefold():
            books_to_return.append(book)

    return books_to_return


# create  request 
@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

# update request
@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

# delete request
@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title:str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get("title").casefold() == book_title.casefold():
            BOOKS.pop(i)
            break


# path parameters
@app.get("/books/author/{author_name}")
async def read_books_by_author(author_name : str):
    books_by_author = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold():
            books_by_author.append(book)
    return books_by_author


# Query parameters
@app.get("/books/author/author_name/")
async def read_books_by_author_query_parameter(author_name:str):
    books_by_author = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold():
            books_by_author.append(book)
    return books_by_author 

# # Query parameters with default value
# @app.get("/books/author/")
# async def read_books_by_author_query_parameter_default(author_name: str = "Author One"):
#     books_by_author = []
#     for book in BOOKS:
#         if book.get("author").casefold() == author_name.casefold():
#             books_by_author.append(book)
#     return books_by_author

# # Query parameters with multiple values
# @app.get("/books/author/multiple")
# async def read_books_by_author_multiple_values(author_name: str = "Author One"):
#     books_by_author = []
#     for book in BOOKS:
#         if book.get("author").casefold() == author_name.casefold():
#             books_by_author.append(book)
#     return books_by_author

# # Query parameters with multiple values and default value
# @app.get("/books/author/multiple/default")
# async def read_books_by_author_multiple_values_default(author_name: str = "Author One"):
#     books_by_author = []
#     for book in BOOKS:
#         if book.get("author").casefold() == author_name.casefold():
#             books_by_author.append(book)
#     return books_by_author

