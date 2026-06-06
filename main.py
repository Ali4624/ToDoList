#Main module
from app_menu import Menu
from dotenv import load_dotenv
import os
load_dotenv(".config.env")
host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
Menu()