from pydantic import BaseModel

class Task(BaseModel):
    id :int 
    task :str
    is_completed: bool=False