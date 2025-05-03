from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: int
    in_stock: bool


external_data = {"id": "94324", "name": "laptop", "price": 94000, "in_stock": True}

product = Product(**external_data)
print(product)
