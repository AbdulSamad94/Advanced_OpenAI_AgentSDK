from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def main(msg: str):
    return {"message": msg}


if __name__ == "__main__":
    uvicorn.run(app)
