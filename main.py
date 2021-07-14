# import fastapi's FastApi class that has all the functionality
# required for our api.
from fastapi import FastAPI


# creates an instance of FastApi
# 'app' is the same one referred by uvicorn in the command
app = FastAPI()


# uses get operation and handles any get request to path / and returns the value
@app.get('/')
async def root():
    return {"message": "Hello World"}


# to run server, type 'uvicorn main:app --reload' in terminal
# Here
# 'uvicorn' is ASGI server implementation
# 'main' is the file name
# 'app' is the instance of FastApi
# '--reload' automatically reloads the server when file is changed