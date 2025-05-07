from pydantic import BaseModel
from typing import List


class Lessons(BaseModel):
    lesson_id: int
    topic: str
    duration: int


class Module(BaseModel):
    model_id: int
    name: str
    lessons: List[Lessons]


class Course(BaseModel):
    course_id: int
    name: str
    modules: List[Module]
