from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class AuthResponse(BaseModel):
    message: str
    username: str


class TodoCreate(BaseModel):
    task: str
    due_date: str


class TodoStatusUpdate(BaseModel):
    status: str  # "COMPLETED" | "CANCELLED" | "PENDING"


class TodoResponse(BaseModel):
    taskId: int
    task: str
    creationTime: str
    expectedCompletion: str
    status: str


class ProfileUpdate(BaseModel):
    name: str
    gender: int  # 1 = Male, 2 = Female
    birthday: str


class ProfileResponse(BaseModel):
    username: str
    name: Optional[str] = None
    gender: Optional[int] = None
    birthday: Optional[str] = None
