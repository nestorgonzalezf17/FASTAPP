from fastapi import FastAPI, Depends
from database import Base, engine
from fastapi.middleware.cors import CORSMiddleware
from Methods import auth
from Models import models

Base.metadata.create_all(bind=engine)

app = FastAPI()
  
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",           
        "http://127.0.0.1:5500",           
        "http://localhost:4200",           
        "http://127.0.0.1:4200"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],  # Incluye OPTIONS
    allow_headers=["*"]
)

@app.get("/ping")

def ping():
    return {"message": "pong"}

app.include_router(auth.router, prefix="/Sesion")