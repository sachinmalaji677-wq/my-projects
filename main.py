#FastAPI 
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello Sachin"}
@app.get("/about")
def about():
    return {"message": "Learning FastAPI"}

@app.get("/student/{id}")
def student(id: int):
    return {"student_id": id}