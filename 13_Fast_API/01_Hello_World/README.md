We use **Uvicorn** with **FastAPI** because:

### 1. **FastAPI needs an ASGI server to run**

- FastAPI is built on the **ASGI** (Asynchronous Server Gateway Interface) standard.
- It doesn’t run by itself — it needs a server that understands ASGI to handle HTTP requests.

### 2. **Uvicorn is an ASGI server**

- Uvicorn is a **lightweight, high-performance ASGI server**.
- It runs FastAPI apps efficiently, especially for modern async Python features.

### 3. **Supports async code**

- FastAPI uses Python’s async/await syntax for better performance.
- Uvicorn supports this async code, while older servers like WSGI ones (used by Flask or Django) don’t.

### 4. **Great for development & production**

- Uvicorn has:

  - Fast startup time
  - Automatic reload (with `--reload` flag)
  - Production support with Gunicorn (`gunicorn -k uvicorn.workers.UvicornWorker`)

---

### Example:

```bash
uvicorn main:app --reload
```

This command tells Uvicorn to:

- Run the `app` object from the `main.py` file
- Auto-reload the server when code changes (useful in development)

---

In short:
**Uvicorn is what actually serves your FastAPI app to the web**, just like how a web browser needs a web server to get and send data.
