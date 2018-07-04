#!/usr/bin/python3

from datetime import datetime
import os.path
import sqlite3
import subprocess as sp

class SQLite:

    def __init__(self):
        """ Database setup. """
        BASE_DIR = os.path.dirname(os.path.abspath(__name__))
        db_path = os.path.join(BASE_DIR, "puppy.sqlite3")
        self.db = sqlite3.connect(db_path)

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


    def actions(self, action_id=None):
        """
            List actions.

            Parameters:
                - action_id (optional): action_id for retrieving specific data
        """
        cursor = self.db.cursor()
        query = None
        if action_id is None
            query = """ SELECT * FROM Actions """
        else:
            query = """ SELECT * FROM Actions
                        WHERE Id='{0}'""".format(action_id)
        cursor.execute(query)
        data = [ row for row in cursor.fetchall() ]
        self.db.commit()
        return data


    def run_action(self, action_id, user):
        """
            Runs an action, based on action_id.

            Parameters:
                - action_id: action_id for running a specfic action
        """
        cursor = self.db.cursor()
        query_action = """ SELECT Name, Action FROM Actions
                           WHERE Id='{0}'""".format(action_id)
        cursor.execute(query_action)
        action_data   = cursor.fetchall()
        action_name   = action_data[0]
        action_result = sp.call(action_data[1])
        if action_resutlt == 0:
            query_action_log  = """ INSERT INTO ActionsLog
            (Name, ReturnCode, RunBy) VALUES
            ('{0}', '{1}', '{2}')""".format(action_name, action_result, User)
            cursor.execute(query_action_log)
        self.db.commit()
        return action_result


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


    def logged_actions(self):
        """
            List logged actions.
        """
        cursor = self.db.cursor()
        query = """ SELECT * FROM ActionsLog """
        cursor.execute(query)
        data = cursor.fetchall()
        self.db.commit()
        return data

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
