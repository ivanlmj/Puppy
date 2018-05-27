#!/usr/bin/python3

from datetime import datetime
import sqlite3

class SQLite:

    def __init__(self):
        """ Database setup. """
        self.db = sqlite3.connect('puppy.sqlite3')

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
            return 2

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

    def initial_setup(self):
        """
            Creates the following tables for initial database setup:
                - Users:    registered users
                - Sessions: controlling sessions of authenticated users
        """
        cursor = self.db.cursor()
        drop_users = """ DROP TABLE IF EXISTS Users """
        drop_sessions = """ DROP TABLE IF EXISTS Sessions """
        cursor.execute(drop_users)
        cursor.execute(drop_sessions)
        users = """ CREATE TABLE Users
        (Id INTEGER PRIMARY KEY,
        FullName TEXT, UserName TEXT, PassWord TEXT,
        CreateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        UpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        admin = """ INSERT INTO
        Users (FullName, UserName, Password)
        VALUES ('Administrator', 'root', 'root') """
        sessions = """ CREATE TABLE Sessions
        (Id INTEGER PRIMARY KEY, UserName TEXT,
        StartTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        EndTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        cursor.execute(users)
        cursor.execute(admin)
        cursor.execute(sessions)
        self.db.commit()
