from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/search")
def search_user(name: str, age: int = 18):
    return {"name": name, "age": age}


if __name__ == "__main__":
    uvicorn.run(app)
