from fastapi import APIRouter, HTTPException
from backend.schemas import TodoCreate, TodoStatusUpdate, TodoResponse
from backend.database import get_connection
from datetime import datetime

router = APIRouter()


@router.get("/{username}", response_model=list[TodoResponse])
def get_all_todos(username: str):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT taskId, task, creationTime, expectedCompletion, status FROM todos WHERE username = %s", (username,))
            rows = cursor.fetchall()
    return [{"taskId": r[0], "task": r[1], "creationTime": str(r[2]), "expectedCompletion": str(r[3]), "status": r[4]} for r in rows]


@router.post("/{username}", response_model=dict)
def create_todo(username: str, body: TodoCreate):
    if len(body.task) > 50:
        raise HTTPException(status_code=400, detail="Task cannot exceed 50 characters")
    creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO todos(username, task, creationTime, expectedCompletion) VALUES(%s,%s,%s,%s)",
                          (username, body.task, creation_time, body.due_date))
            conn.commit()
    return {"message": "Task created"}



@router.patch("/{todo_id}/status", response_model=dict)
def update_status(todo_id: int, body: TodoStatusUpdate):
    if body.status not in ("COMPLETED", "CANCELLED", "PENDING"):
        raise HTTPException(status_code=400, detail="Invalid status")
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE todos SET status = %s WHERE taskId = %s", (body.status, todo_id))
            conn.commit()
    return {"message": "Status updated"}



@router.delete("/{todo_id}", response_model=dict)
def delete_todo(todo_id: int):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM todos WHERE taskId = %s", (todo_id,))
            conn.commit()
    return {"message": "Task deleted"}

