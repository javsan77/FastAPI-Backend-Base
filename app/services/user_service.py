from typing import List
from fastapi import HTTPException, status

from app.schemas.user_schema import UserCreate
from app.repositories.user_repository import UserRepository

_repository = UserRepository()

class UserService:
        def create_user(self, user: UserCreate) -> dict:
            return self.repository.create(user)
        
        def get_all_users(self) -> List[dict]:
            return self.repository.find_all()
        
        def get_user_by_id(self, user_id: int) -> dict:
            user = self.repository.find_by_id(user_id)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
            return user
        
