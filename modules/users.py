#!/usr/bin/python3

from . import database

class User:


    def __init__(self):
        self.db = database.SQLite()


    def login(self, username, password):
        """
            Performs user authentication.

            Parameters:
                - username
                - password

            Returns:
                - 0: login successful
                - 1: login unsuccessful
                - 2: user not found
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ SELECT PassWord FROM Users
                        WHERE UserName='{0}'""".format(username)
            cursor.execute(query)
            data = cursor.fetchone()
            self.db.conn.commit()
            if data:
                if password == data[0]:
                    return 0
                else:
                    return 1
            else:
                return 1
        except Exception as e:
            return e


    def create(self, fullname, username, password):
        """
            Creates a new user.

            Parameters:
                - fullname
                - username
                - password
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ INSERT INTO Users (FullName, UserName, PassWord)
                        VALUES ('{0}', '{1}', '{2}')
                    """.format(fullname, username, password)
            cursor.execute(query)
            self.db.conn.commit()
            return 0
        except Exception as e:
            return e


    def remove(self, username):
        """
            Removes an user.

            Parameters:
                - username
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ DELETE FROM Users
                        WHERE UserName='{0}'""".format(username)
            cursor.execute(query)
            self.db.conn.commit()
            return 0
        except Exception as e:
            return e
