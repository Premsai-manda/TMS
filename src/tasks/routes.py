from fastapi import APIRouter,Depends
from src.tasks import controllers
from src.utils import db
from src.tasks import dtos
from sqlalchemy.orm import Session
from src.tasks import models

task_routes = APIRouter(prefix="/task")



@task_routes.get("/")
def home():
    return {"Status":"This is Task Page"}

@task_routes.get("/all")
def get_all_tasks(db:Session = Depends(db.get_db)):
    return controllers.get_all_task(db)

@task_routes.post("/add")
def add_task(body:dtos.Task, db = Depends(db.get_db)):
    return controllers.add_task(body,db)


@task_routes.get("/get/{id}")
def get_task_by_id(id:int,db = Depends(db.get_db)):
    return controllers.get_task_by_id(id,db)


@task_routes.put("/update/{id}")
def update_task(id:int,body:dtos.Task,db =Depends(db.get_db)):
    return controllers.update_task(id,body,db)

@task_routes.delete("/remove/{id}")
def Remove_task(id:int,db =Depends(db.get_db)):
    return controllers.remove_task(id,db)


