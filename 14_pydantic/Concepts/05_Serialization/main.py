from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import List


class Adress(BaseModel):
    street: str
    city: str
    state: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    registered_at: datetime
    tags: List[str] = []
    addresses: Adress

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime("%d-%m-%Y %H:%M:%S")}
    )


user = User(
    id=1,
    name="Abdul Samad",
    email="6gZKb@example.com",
    registered_at=datetime(2024, 3, 15, 14, 30),
    addresses=Adress(street="abc", city="abc", state="abc"),
    tags=["hello", "world"],
)

# Using model_dump() covert pydantic model to python dict
python_dict = user.model_dump()
print(python_dict)
print("=============================\n")

# Using model_dump_json() covert pydantic model to json
json_str = user.model_dump_json()
print(json_str)
