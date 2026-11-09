from fastapi import FastAPI

from app.db.base import Base
from app.db.database import engine

# Import modeli przed create_all
from app.models import user

app = FastAPI(
    title="My Backend API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API is running"}