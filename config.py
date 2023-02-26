import os

BASE_DIR = os.path.abspath(os.getcwd())
DB_URL = f"sqlite+aiosqlite:///{BASE_DIR}/hexgone.db"
DB_ECHO = True