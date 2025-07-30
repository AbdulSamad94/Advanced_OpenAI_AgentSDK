from fastapi import FastAPI
import uvicorn
from typing import Optional

app = FastAPI()


@app.get("/items/{item_id}")
# if we want to give a parameter optional we set it to = None, if we dont give it that it will show an error
async def read_item(item_id: str, q: Optional[str] = None):
    print(item_id)
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run(app)
