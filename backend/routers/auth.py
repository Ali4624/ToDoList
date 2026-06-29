from fastapi import APIRouter, HTTPException
from backend.schemas import RegisterRequest, LoginRequest, AuthResponse, ProfileUpdate, ProfileResponse
from backend.database import get_connection

router = APIRouter()


@router.post("/register", response_model=AuthResponse)
def register(body: RegisterRequest):
    with get_connection() as conn:
        with conn.cursor() as mycursor:
            mycursor.execute("SELECT username FROM users WHERE username = %s", (body.username,))
            if mycursor.fetchone() is not None:
                raise HTTPException(status_code=400, detail="Username already exists")
            mycursor.execute("INSERT INTO users(username, password) VALUES(%s, %s)", (body.username, body.password))
            conn.commit()
    return {"message": "Registered successfully", "username": body.username}


@router.post("/login", response_model=AuthResponse)
def login(body: LoginRequest):
    with get_connection() as conn:
        with conn.cursor() as my_cursor:
            my_cursor.execute("SELECT password FROM users WHERE username = %s", (body.username,))
            row = my_cursor.fetchone()
            if row is None or row[0] != body.password:
                raise HTTPException(status_code=401, detail="Wrong username or password!")
    return {"message": "Login successful", "username": body.username}


@router.get("/profile/{username}", response_model=ProfileResponse)
def get_profile(username: str):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT username, name, sex, bday FROM users WHERE username = %s", (username,))
            row = cursor.fetchone()
            if row is None:
                raise HTTPException(status_code=404, detail="User not found")
    return {"username": row[0], "name": row[1], "gender": row[2], "birthday": str(row[3]) if row[3] else None}


@router.put("/profile/{username}", response_model=ProfileResponse)
def update_profile(username: str, body: ProfileUpdate):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE users SET name = %s, sex = %s, bday = %s WHERE username = %s",
                          (body.name, body.gender, body.birthday, username))
            conn.commit()
    return {"username": username, "name": body.name, "gender": body.gender, "birthday": body.birthday}

