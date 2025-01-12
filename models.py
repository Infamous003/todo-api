from pydantic import BaseModel
from sqlmodel import SQLModel, Field, String
from datetime import datetime

class Task(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  title: str = Field(String(128), unique=True, nullable=False)
  description: str | None = Field(default=None, max_length=1024, nullable=True)
  due_date: datetime | None = Field(default=None)
  created_at: float = Field(default=datetime.now().timestamp())

class TaskCreate(BaseModel):
  title: str
  description: str | None = None
  due_date: datetime | None = None

class TaskPublic(BaseModel):
  title: str
  description: str
  due_date: datetime

class TaskUpdate(BaseModel):
  title: str | None = None
  description: str | None = None