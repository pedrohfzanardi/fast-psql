import uvicorn
from fastapi import FastAPI

import models
from database import engine
from routes import router as app_router

app = FastAPI()

app.include_router(app_router)

models.Base.metadata.create_all(bind=engine)


@app.get("/health")
def health():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
