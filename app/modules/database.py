
import os.path
import sqlite3

class SQLite:
    """ Provides methods for building SQLite3 connections for Shell-WA.

        Notice:

            depending on your current working directory, instance variable
            "subdir" should be changed, before building a connection object.

        When running dbsetup.py:

            from app.module import database

            db = database.SQLite
            db.subdir = "/app/modules"
            db.connector()
            cursor = db.conn.cursor()
            drop_users = ''' DROP TABLE IF EXISTS Users '''
            cursor.execute(drop_users)

    """

    def __init__(self):
        self.subdir = "/modules"

    def connector(self):
        """ Builds SQLIte URI for the database file (according to your
        current working directory) and builds a connection object.

        """
        db_dir = os.getcwd() + self.subdir
        self.db_path = os.path.join(db_dir, "swa.sqlite3")
        self.conn = sqlite3.connect(self.db_path)
