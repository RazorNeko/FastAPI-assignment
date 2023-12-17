from typing import List

from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str

class Task(BaseModel):
    short_description: str
    detailed_description: str
    status: bool

class UserWithTasks(User):
    tasks: List[Task] = []