from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.routers import auth, todos

my_app = FastAPI(title="ToDoList API")

my_app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
my_app.include_router(todos.router, prefix="/api/todos", tags=["todos"])

my_app.mount("/static", StaticFiles(directory="frontend"), name="static")


@my_app.get("/")
async def serve_frontend():
    return FileResponse("frontend/index.html")
