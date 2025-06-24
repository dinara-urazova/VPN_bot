import pg8000

from bot.config_reader import env_config

with pg8000.connect(
    user=env_config.postgresql_username,
    password=env_config.postgresql_password.get_secret_value(),
    host=env_config.postgresql_hostname,
    port=env_config.postgresql_port,
) as connection:
    print(
        f"[info] Connected to PostgreSQL {env_config.postgresql_hostname}:{env_config.postgresql_port}"
    )
    print(f"[info] Trying to create database {env_config.postgresql_database}...")
    try:
        connection.execute_simple(f"CREATE DATABASE {env_config.postgresql_database}")
        print("[info] OK")
    except Exception as e:
        print(f"[warning] {e}")

with pg8000.connect(
    user=env_config.postgresql_username,
    password=env_config.postgresql_password.get_secret_value(),
    host=env_config.postgresql_hostname,
    port=env_config.postgresql_port,
    database=env_config.postgresql_database,
) as connection:
    print(
        f"[info] Connected to PostgreSQL {env_config.postgresql_hostname}:{env_config.postgresql_port}/{env_config.postgresql_database}"
    )
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS users (
        telegram_id BIGINT PRIMARY KEY NOT NULL,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NULL,
        username VARCHAR(255) NULL,
        created_at TIMESTAMP,
        updated_at TIMESTAMP
        );
    """
    print("[info] Trying to create table users...")
    try:
        connection.execute_simple(sql_create_table)
        print("[info] OK")
    except Exception as e:
        print(f"[error] {e}")
