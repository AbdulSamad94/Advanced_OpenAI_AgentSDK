from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Name of the employee",
        example="Abdul Samad",
    )
    department: Optional[str] = "General"
    salary: float = Field(
        ...,
        ge=100000,
    )


example_input = {
    "id": 1,
    "name": "Abdul Samad",
    "department": "General",
    "salary": 1200000,
}
employee = Employee(**example_input)
print(employee)
