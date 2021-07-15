from enum import Enum
from fastapi import FastAPI

app = FastAPI()


# this is how enum of type string is defined
# enum can be used as ModelName.alexnet
# value of enum can be used as ModelName.value
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


# path param is item_id,
# it is passed as an argument to the function read_item(item_id)
# path param can also be declared with type,
# for eg in this case its of type int

# explicitly mentioning type for the path param enforces data validation
# if the data type is not matched, fastapi will display error
@app.get('/items/{item_id}')
def read_item(item_id: int):
    return {"item_id": item_id}


# path param can also have possible valid path parameter values
# for this we use standard python Enum
@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


# path parameters containing paths
@app.get('/files/{file_path:path}')
async def read_files(file_path: str):
    return {"file_path": file_path}
