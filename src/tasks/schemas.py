from pydantic import BaseModel


class Item(BaseModel):
    build: str
