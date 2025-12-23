from sqlalchemy import text
from app.config.database import get_connection

class UserRepository:

    def create(self, name: str, email: str) -> int:
        with get_connection() as conn:
            result = conn.execute(
                text("EXEC dbo.usp_user_create :name, :email"),
                {"name": name, "email": email}
            )
            return int(result.scalar())

    def find_all(self):
        with get_connection() as conn:
            result = conn.execute(
                text("EXEC dbo.usp_user_list")
            )
            return result.fetchall()

    def find_by_id(self, user_id: int):
        with get_connection() as conn:
            result = conn.execute(
                text("EXEC dbo.usp_user_get_by_id :id"),
                {"id": user_id}
            )
            return result.fetchone()
