from src.tasks import dtos
from src.utils import db
from sqlalchemy.orm import Session
from src.tasks import models

def get_all_task(db):
    all_tasks = db.query(models.taskModel).all()
    return all_tasks



def add_task(body:dtos.Task,db:Session):
    print(body.model_dump())
    new_task = body.model_dump()
    db.add(models.taskModel(**new_task))
    db.commit()
    return {"Status":"task aded sucsessfully..","data":new_task}


# @app.post("/add-book")
# def add_book(book:book, db: Session =Depends(get_db)):
#     db.add(dbmodels.book(**book.model_dump()))
#     db.commit()
#     return book

def get_task_by_id(id,db:Session):
    task = db.query(models.taskModel).get(id)
    if task :
        return {"Status": "Sucsessful","Task":task}
    else:
        return {"Status": "Sucsessful", "result":"Data not Found"}


def update_task(id,body:dtos.Task,db:Session):
    task = db.query(models.taskModel).get(id)
    if task:
        task.task = body.task
        task.is_completed = body.is_completed
        db.add(task)
        db.commit()
        return {"Status":"Sucsessful", "updated task":task}
    else : 
        return {"Status":"no task eith {id}"}

def remove_task(id:int,db:Session):
    task = db.query(models.taskModel).get(id)
    db.delete(task)
    db.commit()
    return {"Status":"Sucsessful" ,"msg":"Task Removed"}
