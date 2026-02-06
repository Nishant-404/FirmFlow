from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes.client import router as client_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(client_router)

@app.get("/")
def root():
    return {"status1": "ok"}
