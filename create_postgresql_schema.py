import pg8000
from bot.config_reader import env_config

connection = pg8000.connect(
    user=env_config.postgresql_username,
    password=env_config.postgresql_password,
    host=env_config.postgresql_hostname,
    port=env_config.postgresql_port,
    database=env_config.postgresql_database,
)

cursor = connection.cursor()

sql_create_table = """
CREATE TABLE IF NOT EXISTS users (
    telegram_id BIGINT PRIMARY KEY NOT NULL,
    first_name VARCHAR(255) NOT NULL, 
    last_name VARCHAR(255) NULL,
    username VARCHAR(255) NULL, 
    created_at TEXT, 
    updated_at TEXT
    );
"""

cursor.execute(sql_create_table)
connection.commit()

cursor.close()
connection.close()
