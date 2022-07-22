from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello():
    return {"message": "Simple app working"}


# Run command
# uvicorn src.app:app --reload