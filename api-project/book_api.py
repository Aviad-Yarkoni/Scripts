
from fastapi import FastAPI
import json


app = FastAPI()

json_file = "/home/osboxes/scripts/api-project/labrary_books.json"
file = open(json_file)
book_list = json.load(file)  

 
@app.get("/book")
def search_instructions():
    instructions = ['hello',
                    'You can search by book title - /book/<bookname>',
                    'You can see the entire list of books - /book/list']
    return instructions


@app.get("/book/{book_name}")
def get_book_name (book_name):
    book_founds = []
    for current_book in book_list:
        if current_book["book"] == book_name:
            book_founds.append(current_book)
        if book_name == 'list':
            book_founds.append(current_book)
    if len(book_founds)== 0:
        book_founds.append('No books found')
    return book_founds




#run web server 
#uvicorn book_api:app --reload

