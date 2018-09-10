
import os.path
import sqlite3

class SQLite:

    def __init__(self):
        """ Database setup. """
        BASE_DIR = os.path.dirname(os.path.abspath(__name__)) + "/modules"
        self.db_path = os.path.join(BASE_DIR, "puppy.sqlite3")
        self.conn = sqlite3.connect(self.db_path)
        print("DB PATH:", self.db_path)
        print("DB CONN:", self.conn)
