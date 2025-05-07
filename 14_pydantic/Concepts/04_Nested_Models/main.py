from pydantic import BaseModel
from typing import List, Optional


class Adress(BaseModel):
    street: str
    city: str
    state: str


class User(BaseModel):
    id: int
    name: str
    addresses: List[Adress]


class Comments(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comments"]] = None


adress = Adress(street="abc", city="abc", state="abc")
user = User(id=1, name="Abdul Samad", addresses=[adress])
print(user)

comments = Comments(
    id=1,
    content="hello",
    replies=[
        Comments(id=2, content="hello"),
        Comments(id=3, content="hello"),
    ],
)
print(comments)
