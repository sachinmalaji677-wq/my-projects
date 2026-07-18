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

#___________________________________________________________________________________________________


# from fastapi import FastAPI
# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# # PostgreSQL connection
# DATABASE_URL = "postgresql://postgres:sde2@localhost:5432/taskdb"

# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# class Task(Base):
#     __tablename__ = "tasks"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)

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


#____________________________________________________________________________________________
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from auth import hash_password, verify_password, create_token, verify_token

DATABASE_URL = "postgresql://taskdb_prod_zlf0_user:x8WU8uUemrN29OGEwjFKjeEzMSTGtRAm@dpg-d9dnecf41pts73dgtk9g-a/taskdb_prod_zlf0"

import os

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:sde2@localhost:5432/taskdb"
)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# User Model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

# Task Model
class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    owner_email = Column(String)

Base.metadata.create_all(bind=engine)

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Register
@app.post("/register")
def register(email: str, password: str):
    db = SessionLocal()
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        db.close()
        raise HTTPException(status_code=400, detail="Email already registered!")
    hashed = hash_password(password)
    user = User(email=email, password=hashed)
    db.add(user)
    db.commit()
    db.close()
    return {"message": "Registered successfully!"}

# Login
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.email == form_data.username).first()
    db.close()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials!")
    token = create_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

# Get current user from token
def get_current_user(token: str = Depends(oauth2_scheme)):
    email = verify_token(token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token!")
    return email

# Protected Tasks
@app.post("/tasks")
def create_task(title: str, current_user: str = Depends(get_current_user)):
    db = SessionLocal()
    task = Task(title=title, owner_email=current_user)
    db.add(task)
    db.commit()
    db.refresh(task)
    db.close()
    return {"id": task.id, "title": task.title, "owner": current_user}

@app.get("/tasks")
def get_tasks(current_user: str = Depends(get_current_user)):
    db = SessionLocal()
    tasks = db.query(Task).filter(Task.owner_email == current_user).all()
    db.close()
    return {"tasks": tasks}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: str = Depends(get_current_user)):
    db = SessionLocal()
    task = db.query(Task).filter(Task.id == task_id, Task.owner_email == current_user).first()
    if task:
        db.delete(task)
        db.commit()
        db.close()
        return {"message": "Deleted!"}
    db.close()
    return {"error": "Not found!"}