from fastapi import FastAPI, HTTPException, status
from models import Task, TaskPublic, TaskCreate, TaskUpdate
from sqlmodel import Session, select
from datetime import datetime
from db import create_db_and_tables, mydb

app = FastAPI()
create_db_and_tables()

@app.get("/")
def index():
  return {"Hello": "World"}

@app.get("/tasks")
def get_tasks() -> list[Task]:
  with Session(mydb) as session:
    statement = select(Task)
    tasks = session.exec(statement).fetchall()
    return tasks

@app.get("/tasks/{id}")
def get_tasks(id: int) -> TaskPublic:
  with Session(mydb) as session:
    statement = select(Task).where(Task.id == id)
    taskExists = session.exec(statement).one_or_none()

    if not taskExists:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    return taskExists

@app.post("/tasks")
def create_tasks(task: TaskCreate):
  new_task = Task(**task.model_dump())
  with Session(mydb) as session: 
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task
  
@app.delete("/tasks/{id}")
def delete_task(id: int):
  with Session(mydb)as session:
    statement = select(Task).where(Task.id == id)
    taskExists = session.exec(statement).one_or_none()

    if not taskExists:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")
    session.delete(taskExists)
    session.commit()

@app.put("/tasks/{id}")
def update_task(id: int, task: TaskUpdate):
  with Session(mydb)as session:
    statement = select(Task).where(Task.id == id)
    taskExists = session.exec(statement).one_or_none()

    if not taskExists:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="task not found")

    if task.title: taskExists.title = task.title
    if task.description: taskExists.description = task.description

    session.add(taskExists)
    session.commit()
    session.refresh(taskExists)
    return taskExists