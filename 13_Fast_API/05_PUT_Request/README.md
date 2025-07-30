### ✅ What is a PUT Request?

- A **PUT** request is used to **update** an existing resource (like a user, a product, or any item).
- In REST APIs, `PUT` is used when you want to **replace or modify** a specific item using its **ID**.

---

### 🧠 Example Scenario:

Let’s say you have a list of users stored in your database, and each user has a unique ID.
If you want to **update user #2's name or email**, you will send a PUT request to `/users/2`.

---

### 🧪 Sample Code in FastAPI

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Data model
class User(BaseModel):
    name: str
    email: str

# Dummy database (list)
users = [
    {"id": 1, "name": "Samad", "email": "samad@example.com"},
    {"id": 2, "name": "Ali", "email": "ali@example.com"},
]

@app.put("/users/{user_id}")
def update_user(user_id: int, updated_user: User):
    for user in users:
        if user["id"] == user_id:
            user["name"] = updated_user.name
            user["email"] = updated_user.email
            return {"message": "User updated", "user": user}
    raise HTTPException(status_code=404, detail="User not found")
```

---

### 📥 Example Request:

**URL**: `PUT /users/2`
**Body** (JSON):

```json
{
  "name": "Updated Ali",
  "email": "updated.ali@example.com"
}
```

---

### 📤 Example Response:

```json
{
  "message": "User updated",
  "user": {
    "id": 2,
    "name": "Updated Ali",
    "email": "updated.ali@example.com"
  }
}
```

---

### 📌 Summary:

| Point                        | Detail                         |
| ---------------------------- | ------------------------------ |
| **Method**                   | PUT                            |
| **Purpose**                  | To update an existing resource |
| **Requires**                 | ID in URL + New data in body   |
| **Status code if not found** | 404                            |
