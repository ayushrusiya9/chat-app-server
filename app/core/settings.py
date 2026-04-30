from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # APP DESCRIPTION
    APP_NAME = "CHAT APP"
    APP_DESCRIPTION = "A simple chat application"

    # DATABASE CONFIG
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")

    # jwt config
    SECRET_KEY= os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


settings = Settings()

