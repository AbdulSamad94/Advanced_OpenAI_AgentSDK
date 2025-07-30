In **FastAPI**, **path parameters** are parts of the URL path that are **dynamic** — they let you accept input directly from the URL.

---

### 🔹 Example URL with path parameter:

```http
/items/42
```

Here, `42` is a path parameter — usually representing something like an item ID.

---

### 🔹 How to define path parameters in FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

#### ✅ Explanation:

- `/items/{item_id}`: This defines a **path parameter** named `item_id`.
- `item_id: int`: FastAPI will **automatically convert** it to an `int` and **validate** it.
- When you visit `/items/42`, it returns: `{"item_id": 42}`.

---

### 🔹 Multiple path parameters:

```python
@app.get("/users/{user_id}/orders/{order_id}")
async def get_order(user_id: int, order_id: int):
    return {"user_id": user_id, "order_id": order_id}
```

URL: `/users/7/orders/100` → returns: `{"user_id": 7, "order_id": 100}`

---

### 🔹 Type validation:

FastAPI supports many types (like `int`, `float`, `str`, `UUID`, `datetime`, etc.)

```python
from uuid import UUID

@app.get("/items/{item_id}")
async def read_item(item_id: UUID):
    return {"item_id": item_id}
```

---

### 🔹 Summary:

| Feature         | Description                      |
| --------------- | -------------------------------- |
| `{param}`       | Declares a path parameter        |
| Type hints      | Automatically validate & convert |
| Multiple params | Supported in same URL            |
| Used for        | IDs, usernames, slugs, etc.      |

---
