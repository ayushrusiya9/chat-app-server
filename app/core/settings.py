from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    # APP DESCRIPTION
    APP_NAME = "CHAT APP"
    APP_DESCRIPTION = "A simple chat application"

    # DATABASE CONFIG
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    PASSWORD = os.getenv("DB_PASSWORD")
    NAME = os.getenv("DB_NAME")
    USER = os.getenv("DB_USER")

    # jwt config
    SECRET_KEY= os.getenv("SECRET_KEY")
    ALGORITHM = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


settings = Settings()

