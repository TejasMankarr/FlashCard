from fastapi import FastAPI
from database.connection import engine, Base
from routes import auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Authentication API!"}

# Include authentication routes
app.include_router(auth.router)