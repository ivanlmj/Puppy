
import os.path
import sqlite3

class SQLite:

    def __init__(self):
        """ Database setup. """
        # add modules path here (+++)
        #   DB PATH: /home/ivanlmj/git/Puppy/puppy.sqlite3
        #   DB CONN: <sqlite3.Connection object at 0x7ff07bc31ab0>
        #   DB Path: /home/ivanlmj/git/Puppy/puppy.sqlite3
        #   DB Conn: <sqlite3.Connection object at 0x7ff07bc31ab0>
        BASE_DIR = os.path.dirname(os.path.abspath(__name__)) + "/modules"
        self.db_path = os.path.join(BASE_DIR, "puppy.sqlite3")
        self.conn = sqlite3.connect(self.db_path)
        print("DB PATH:", self.db_path)
        print("DB CONN:", self.conn)
