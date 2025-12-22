from typing import List
from fastapi import APIRouter

from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import UserService

router = APIRouter()
service = UserService()

@router.post("/", response_model=UserResponse)
def create_user(user:UserCreate):
    return service.create_user(user)

@router.get("/", response_model=List[UserResponse])
def get_users():
    return service.get_all_users()

@router.get("{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    return service.get_user_by_id(user_id)
