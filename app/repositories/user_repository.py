from typing import List, Optional
from app.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self):
        self._users: List[dict] = []
        self._id_counter: int = 1

    def create(self, user: UserCreate)->dict:
        new_user = {
            "id": self._id_counter,
            "name": user.name,
            "email": user.email
        }
        self._users.append(new_user)
        self._id_counter += 1
        return new_user
    
    def find_all(self) -> List[dict]:
        return self._users
    
    def find_by_id(self, user_id:int)->Optional[dict]:
        for user in self._users:
            if user["id"] == user_id:
                return user
            return None
