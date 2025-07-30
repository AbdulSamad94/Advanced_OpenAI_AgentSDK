In **FastAPI**, a **query parameter** is a value that is passed in the **URL after the `?` symbol** — used to **filter, sort, or search** data.

---

### 🔹 Example URL with query parameter:

```
/items?name=pen
```

Here, `name=pen` is a **query parameter**.

---

### 🔹 How to define query parameters:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
async def read_item(name: str):
    return {"name": name}
```

#### ✅ Explanation:

- The endpoint is `/items`, not `/items/{something}`
- But we define `name: str` in the function → this makes `name` a **query parameter**
- Visiting `/items?name=pen` returns:

  ```json
  { "name": "pen" }
  ```

---

### 🔹 Multiple query parameters:

```python
@app.get("/items")
async def read_item(name: str, price: float):
    return {"name": name, "price": price}
```

URL:

```
/items?name=pen&price=10.5
```

---

### 🔹 Optional query parameters:

```python
from typing import Optional

@app.get("/items")
async def read_item(name: Optional[str] = None):
    return {"name": name}
```

Now `/items` works **with or without** `?name=...`

---

### 🔹 With default value:

```python
@app.get("/items")
async def read_item(name: str = "default"):
    return {"name": name}
```

If no name is given, it will return:

```json
{ "name": "default" }
```

---

### 🔹 Summary:

| Feature                | Description                                   |
| ---------------------- | --------------------------------------------- |
| Comes after `?` in URL | `/items?name=pen`                             |
| Defined in function    | Just use a regular parameter like `name: str` |
| Optional               | Use `Optional` or default values              |
| Used for               | Filtering, searching, pagination, etc.        |

---
