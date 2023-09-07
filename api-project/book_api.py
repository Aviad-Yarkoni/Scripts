
from fastapi import FastAPI
import json


# app = FastAPI()
# def main_book_api ():
#     labrary_books_file = "~/scripts/api-project/labrary_books"
#     labrary_books = load_json_file("a")


def read_json_file():
    json_file = "/home/osboxes/scripts/api-project/labrary_books.json"
    with open(json_file, "r") as file:
        data = json.load(file)  
    return data


def read_json_file2():
    json_file = "/home/osboxes/scripts/api-project/labrary_books.json"
    file = open(json_file)
    data = json.load(file)  
    return data
  
# @app.get("/")
# def root():
#     return {"message": "Hello book"}


# @app.get("/book/{book_name}")
# def get_book_name (book_name):
#     return {"book":book_name }


a = read_json_file2()
print (a)
json_file = "/home/osboxes/scripts/api-project/labrary_books.json"



#run web server 
#uvicorn book_api:app --reload

