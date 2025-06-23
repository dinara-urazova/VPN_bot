import pg8000
from bot.config_reader import env_config


class PostgreSQLSingleton:
    _connection = None

    @classmethod
    def getConnection(cls):
        if cls._connection is None:
            cls._connection = pg8000.connect(
                user=env_config.postgresql_username,
                password=env_config.postgresql_password.get_secret_value(),
                host=env_config.postgresql_hostname,
                port=env_config.postgresql_port,
                database=env_config.postgresql_database,
            )

        return cls._connection
