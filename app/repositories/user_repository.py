from typing import List, Optional
from sqlalchemy import text
from app.config.database import get_connection
from app.schemas.user_schema import UserCreate

class UserRepository:
    def __init__(self):
        self._users: List[dict] = []
        self._id_counter: int = 1

    def create(self, user: UserCreate)->int:
        sql = text("""
            EXEC dbo.usp_user_create
                @Name = :name,
                @Email = :email
            """)

        with get_connection() as conn:
            result = conn.execute(sql, {
                "name": user.name,
                "email": user.email
            })
            new_id = result.scalar()
            conn.commit()        

        return new_id
    
    def find_all(self) -> List[dict]:
        sql = text("EXEC dbo.usp_user_list")

        with get_connection() as conn:
            result = conn.execute(sql)
            rows = result.mappings.all()

        return rows
    
    def find_by_id(self, user_id:int)->Optional[dict]:
        sql = text("""
                EXEC dbo.usp_user_get_by_id
                @Id  = :id
            """)

        with get_connection() as conn:
            result = conn.execute(sql, {"id":user_id})
            row = result.mappings().first()
        
        return dict(row) if row else None


