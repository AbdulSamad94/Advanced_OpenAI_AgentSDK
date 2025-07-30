from fastapi import FastAPI, APIRouter
import uvicorn
from pydantic import BaseModel
import random

router = APIRouter()
app = FastAPI()

data = []


class Person(BaseModel):
    id: int = None
    name: str
    profession: str


@router.get("/")
async def read_root():
    return {"message": "Welcome to the API!"}


@router.get("/people")
async def get_people():
    return data


@router.post("/add_person")
async def add_person(person: Person):
    user_id = random.randint(1000, 9999)
    person.id = user_id
    data.append(person)
    return {"message": "Person added successfully", "person": person}


@router.put("/update_user/{user_id}")
async def update_user(user_id: int, person: Person):
    for i in data:
        if i.id == user_id:
            i.id = user_id
            i.name = person.name
            i.profession = person.profession
            return {"message": "Person updated successfully"}


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app)
