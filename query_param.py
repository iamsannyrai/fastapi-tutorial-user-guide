from typing import Optional
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {
    "iten_name": "Bar"}, {"item_name": "Baz"}]


# declaring function parameters that are not
# part of path parameters are considered query parameters
@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip+limit]


# optional parameters
@app.get("/items/{item_id}")
async def read_item_second_way(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


# multiple path parameters and multiple query parameters
# short is required query parameter, any query param that
# doesnot have default value or is not set None is required
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, short: bool, q: Optional[str] = None
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
