# FastAPI 
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello Sachin"}
# @app.get("/about")
# def about():
#     return {"message": "Learning FastAPI"}

# @app.get("/student/{id}")
# def student(id: int):
#     return {"student_id": id}



# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/login")
# async def root():
#     return {"message": "Hello sachin"}


# @app.get("/posts")
# async def get_posts():
#     return {"message": "Here are your posts"}


# from fastapi import FastAPI
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# Database setup
# DATABASE_URL = "sqlite:///./tasks.db"
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # Task Model (Table)
# class Task(Base):
#     __tablename__ = "tasks"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)

# # Create table
# Base.metadata.create_all(bind=engine)

# app = FastAPI()

# @app.post("/tasks")
# def create_task(title: str):
#     db = SessionLocal()
#     task = Task(title=title)
#     db.add(task)
#     db.commit()
#     db.refresh(task)
#     db.close()
#     return {"id": task.id, "title": task.title}

# @app.get("/tasks")
# def get_tasks():
#     db = SessionLocal()
#     tasks = db.query(Task).all()
#     db.close()
#     return {"tasks": tasks}

# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     db = SessionLocal()
#     task = db.query(Task).filter(Task.id == task_id).first()
#     if task:
#         db.delete(task)
#         db.commit()
#         db.close()
#         return {"message": "Deleted!"}
#     db.close()
#     return {"error": "Not found!"}




from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# PostgreSQL connection
DATABASE_URL = "postgresql://postgres:sde2@localhost:5432/taskdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/tasks")
def create_task(title: str):
    db = SessionLocal()
    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return {"id": task.id, "title": task.title}

@app.get("/tasks")
def get_tasks():
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    return {"tasks": tasks}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
        db.close()
        return {"message": "Deleted!"}
    db.close()
    return {"error": "Not found!"}