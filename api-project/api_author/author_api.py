
from fastapi import FastAPI
import json


app = FastAPI()

json_file = "/author_api/labrary_books.json"
file = open(json_file)
author_list = json.load(file)  



@app.get("/")
def get_root():
    instructions = ['Hello',
                    'You can search by book title - /book/<book name>',
                    'You can search by author name - /author/<author name>',
                    'You can see the entire list of authors - /author/list']
    return instructions

 
@app.get("/author")
def search_instructions():
    instructions = ['You can search by author name - /author/<authorname>',
                    'You can see the entire list of authors - /author/list']
    return instructions


@app.get("/author/{author_name}")
def get_author_name (author_name):
    author_founds = []
    for current_author in author_list:
        if current_author["author"] == author_name:
            author_founds.append(current_author)
        if author_name == 'list':
            author_founds.append(current_author)
    if len(author_founds)== 0:
        author_founds.append('No authors found')
    return author_founds


#run web server 
#uvicorn author_api:app --reload


