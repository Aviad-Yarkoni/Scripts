
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello book"}


@app.get("/book/{book_name}")
async def root(book_name):
    return {"book":book_name }




#for web server run shell below
#uvicorn book_api:app --reload

