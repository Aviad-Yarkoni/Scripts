
from fastapi import FastAPI
import labary_books 




app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello book"}


@app.get("/book/{book_name}")
def get_book_name (book_name):
    return {"book":book_name }




#for web server run shell below
#uvicorn book_api:app --reload

