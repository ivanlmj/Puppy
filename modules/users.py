#!/usr/bin/python3

import database

class Users:


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
        cursor = self.db.cursor()
        query = """ SELECT PassWord FROM Users
                    WHERE UserName='{0}'""".format(username)
        cursor.execute(query)
        data = cursor.fetchone()
        self.db.commit()
        if data:
            if password == data[0]:
                return 0
            else:
                return 1
        else:
            return 1


    def create_user(self, fullname, username, password):
        """
            Creates a new user.

            Parameters:
                - fullname
                - username
                - password
        """
        cursor = self.db.cursor()
        query = """ INSERT INTO Users (FullName, UserName, PassWord) VALUES
             ('{0}', '{1}', '{2}') """.format(fullname, username, password)
        cursor.execute(query)
        self.db.commit()
