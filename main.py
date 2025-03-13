from task_model import Task
from fastapi import FastAPI

app = FastAPI()

tasks = [
    Task(),
    Task()
]

@app.get("/")
def root():
    return "Hello World"

@app.get("/get-all-tasks")
def get_tasks():
    return "Hello World"

@app.get("/get-all-tasks")
def get_all_tasks():
    return tasks

@app.put("/")
def root():
    return "Hello World"

@app.post("/")
def create_task():
    return "Hello World"

@app.delete("/")
def delete_task():
    return "Hello World"

