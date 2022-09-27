# python3 -m venv /path/to/new/virtual/environment
# fish  -> $ source <venv>/bin/activate.fish

# python3 -m venv ~/python/pythonvirtual
# source ~/python/pythonvirtual/bin/activate.fish 

# pip install fastapi
# pip install "uvicorn[standard]"

from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# run inside fastapi folder
# uvicorn main:app --reload