from pydantic import BaseSettings


class Settings(BaseSettings):
    database_hostname: str
    database_name: str
    database_port: str
    database_username: str
    database_password: str

    class Config:
        # hidden in /app
        env_file = ".env_local"


settings = Settings()  # type: ignore
