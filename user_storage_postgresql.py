import pg8000
from user import User
from datetime import datetime, timezone
from bot.config_reader import env_config
from typing import List


def get_connection():
    with pg8000.connect(
        user=env_config.postgresql_username,
        password=env_config.postgresql_password.get_secret_value(),
        host=env_config.postgresql_hostname,
        port=env_config.postgresql_port,
        database=env_config.postgresql_database,
    ) as connection:
        yield connection


class UserStoragePostgreSQL:

    def get_all_users(self) -> List[User]:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        users = []
        for row in rows:
            user = User(
                telegram_id=row[0],
                first_name=row[1],
                last_name=row[2],
                username=row[3],
                created_at=row[4],
                updated_at=row[5],
            )
            users.append(user)
            return users

    def user_exists(self, telegram_id: int) -> bool:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT telegram_id FROM users WHERE telegram_id = %s", [telegram_id]
        )
        res = cursor.fetchone()  # либо None, либо telegram_id
        return res is not None

    def add_user(self, user: User) -> None:
        created_at = updated_at = datetime.now(timezone.utc).isoformat()
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
        INSERT INTO users (telegram_id, first_name, last_name, username, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)
        """,
            [
                user.telegram_id,
                user.first_name,
                user.last_name,
                user.username,
                created_at,
                updated_at,
            ],
        )
        connection.commit()
