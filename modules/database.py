#!/usr/bin/python3

from datetime import datetime
import sqlite3

class SQLite:

    def __init__(self):
        self.db = sqlite3.connect('puppy.sqlite3')
        self.db.close()

    def login(self, username, password):
        cursor = self.db.cursor()
        query = """ SELECT PassWord FROM Auth 
                    WHERE UserName='{0}'
                """.format(username)
        cursor.execute(query)
        data = cursor.fetchone()
        db.commit()
        if data:
            if password == data:
                return 0
            else:
                return 1

    def create_user(self, fullname, username, password):
        ts = datetime.now()
        cursor = self.db.cursor()
        query = """ INSERT INTO Auth 
                    (FullName, UserName, PassWord, Created, Modified) 
                    VALUES ({0}, {1}, {2}, {3}, {4})
                """.format(fullname, username, password, ts, ts)
        cursor.execute(query)
        db.commit()
