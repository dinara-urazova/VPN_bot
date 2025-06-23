from user import User
from datetime import datetime, timezone
from postgresql_singleton import PostgreSQLSingleton
from typing import List


class UserStoragePostgreSQL:

    def get_all_users(self) -> List[User]:
        result = PostgreSQLSingleton.getConnection().run("SELECT * FROM users")

        users = []
        for row in result:
            user = User(
                telegram_id=row[0],
                first_name=row[1],
                last_name=row[2],
                username=row[3],
                created_at=row[4],
                updated_at=row[5],
            )
            users.append(user)
        print(users)
        return users

    def user_exists(self, telegram_id: int) -> bool:
        result = PostgreSQLSingleton.getConnection().run(
            f"SELECT 1 FROM users WHERE telegram_id = {telegram_id}"  # мб unsafe (sql_injections) и дб параметризация, но ее нет в pg8000.native
        )
        return bool(result) # True if there's a user  - list with 1, False if None (empty list)

    def add_user(self, user: User) -> None:
        created_at = updated_at = datetime.now(timezone.utc).isoformat()
        PostgreSQLSingleton.getConnection().run(
            f"""
            INSERT INTO users (telegram_id, first_name, last_name, username, created_at, updated_at) VALUES (
                {user.telegram_id},
                '{user.first_name}',
                '{user.last_name}',
                '{user.username}',
                '{created_at}',
                '{updated_at}'
            )
            """
        )
