from fastapi import FastAPI
import uvicorn
from routes import router as app_router

app = FastAPI()

app.include_router(app_router)


@app.get("/health")
def health():
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
