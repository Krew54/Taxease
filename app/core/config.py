import pathlib
from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    db_host: str = os.environ.get('DB_HOST')
    db_port: str = os.environ.get('DB_PORT')
    db_username: str = os.environ.get('DB_USERNAME')
    db_password: str = os.environ.get("DB_PASSWORD")
    db_name: str = os.environ.get('DB_NAME')
    mail_jet_api_key: str = os.environ.get('MAIL_JET_API_KEY')
    mail_jet_api_secret_key: str = os.environ.get('MAIL_JET_API_SECRET_KEY')
    salt=os.environ.get("SALT")
    jwt_secret_key=os.environ.get("JWT_SECRET_KEY")
    jwt_algorithm=os.environ.get("ALGORITHM")
    jwt_access_token_expires=os.environ.get("JWT_ACCESS_TOKEN_EXPIRES", 30)
   


def get_settings():
    return Settings()