# when we send data to api, it is sent as Request Body
# when data is received from api, it is Response Body

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel  # imports Pydantic's BaseModel


# creates data model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post('/items/')
async def create_item(item: Item):  # declare item as parameter
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
