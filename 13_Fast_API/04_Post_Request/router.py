from fastapi import APIRouter, FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None


app = FastAPI()
router = APIRouter()

data = []


@router.post("/items/")
def create_item(item: Item):
    data.append(item)
    return item


@router.get("/")
def read_items():
    return data


app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port={8001})
