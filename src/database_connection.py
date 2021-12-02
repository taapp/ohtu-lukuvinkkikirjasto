import sqlite3
from pathlib import Path

def create_data_directory(dir_path):
    if not dir_path.exists():
        dir_path.mkdir()

DATA_DIRECTORY_PATH = Path(__file__).parent / "data"
create_data_directory(DATA_DIRECTORY_PATH)
DATABASE_FILE_PATH = DATA_DIRECTORY_PATH / "database.db"
CONNECTION = sqlite3.connect(DATABASE_FILE_PATH)
CONNECTION.row_factory = sqlite3.Row


def get_database_connection():
    return CONNECTION
