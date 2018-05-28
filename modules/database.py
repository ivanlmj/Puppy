#!/usr/bin/python3

from datetime import datetime
import sqlite3

class SQLite:

    def __init__(self):
        """ Database setup. """
        self.db = sqlite3.connect('../puppy.sqlite3')

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

    def create_action(self, name, action):
        """
            Creates a new action.

            Parameters:
                - name:   action name
                - action: command that executes the action
        """
        cursor = self.db.cursor()
        query = """ INSERT INTO Actions (Name, Action) VALUES
                    ('{0}', '{1}') """.format(name, action)
        cursor.execute(query)
        self.db.commit()

    def remove_action(self, name):
        """
            Removes an action.

            Parameters:
                - name:   action name
        """
        cursor = self.db.cursor()
        query = """ DELETE FROM Actions WHERE Name='{0}'""".format(name)
        cursor.execute(query)
        self.db.commit()

    def list_actions(self):
        """
            List actions.
        """
        cursor = self.db.cursor()
        query = """ SELECT * FROM Actions """
        cursor.execute(query)
        self.db.commit()

    def initial_setup(self):
        """
            Creates the following tables for initial database setup:
                - Users:    registered users
                - Sessions: controlling sessions of authenticated users
        """
        cursor = self.db.cursor()
        # queries
        drop_users = """ DROP TABLE IF EXISTS Users """
        drop_sessions = """ DROP TABLE IF EXISTS Sessions """
        drop_actions = """ DROP TABLE IF EXISTS Actions """
        create_users = """ CREATE TABLE Users
        (Id INTEGER PRIMARY KEY,
        FullName TEXT, UserName TEXT, PassWord TEXT,
        CreateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        UpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        create_sessions = """ CREATE TABLE Sessions
        (Id INTEGER PRIMARY KEY, UserName TEXT,
        StartTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        EndTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        create_actions = """ CREATE TABLE Actions
        (Id INTEGER PRIMARY KEY, Name TEXT, Action TEXT,
        CreateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        UpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        log_actions = """ CREATE TABLE LogActions
        (Id INTEGER PRIMARY KEY, ActionName TEXT, RunBy TEXT,
        CreateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        UpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        add_admin = """ INSERT INTO
        Users (FullName, UserName, Password)
        VALUES ('Administrator', 'root', 'root') """
        # execution
        cursor.execute(drop_users)
        cursor.execute(drop_sessions)
        cursor.execute(create_users)
        cursor.execute(create_sessions)
        cursor.execute(create_actions)
        cursor.execute(log_actions)
        cursor.execute(add_admin)
        self.db.commit()
