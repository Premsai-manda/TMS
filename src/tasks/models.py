from sqlalchemy import Column,Integer,String,Boolean
from src.utils.db import Base

class taskModel(Base):
    __tablename__ = "Task"

    id = Column(Integer,unique=True,primary_key=True)
    task = Column(String)
    is_completed = Column(Boolean, default=False)
