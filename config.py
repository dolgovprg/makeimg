from pydantic import BaseSettings

class Settings(BaseSettings):

    SQLALCHEMY_DATABASE_URL: str = "postgresql://postgres:postgres@localhost/instagram"

    ALLOW_ORIGINS : str = "http://localhost:8080"
    MAIN_URL: str = "http://localhost:8000"

settings = Settings()
