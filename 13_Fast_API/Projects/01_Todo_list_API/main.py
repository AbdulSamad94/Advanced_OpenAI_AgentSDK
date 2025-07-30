from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
import uvicorn


class Todo(BaseModel):
    task: str
    completed: bool = False


todos = []

app = FastAPI()
route = APIRouter()


@route.post("/add_todo")
async def add_todo(todo: Todo):
    todos.append(todo)
    return todo


@route.get("/")
async def home():
    return [{"message": "Working Perfectly"}, todos]


app.include_router(route)

if __name__ == "__main__":
    uvicorn.run(app)
