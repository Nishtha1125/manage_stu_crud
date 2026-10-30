from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=1)
    course: str
    marks: float


class Student(BaseModel):
    id: int
    name: str
    course: str
    marks: float
