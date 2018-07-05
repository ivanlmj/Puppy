import os.path
import sqlite3

class SQLite:

    def __init__(self):
        """ Database setup. """
        BASE_DIR = os.path.dirname(os.path.abspath(__name__))
        db_path = os.path.join(BASE_DIR, "puppy.sqlite3")
        self.conn = sqlite3.connect(db_path)
