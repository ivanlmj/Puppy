#!/usr/bin/python3

import database

db = database.SQLite()

def run(self):
        """
            Creates tables for initial database setup:
                - Users:      user management
                - Sessions:   controlling sessions of authenticated users
                - Actions:    commands exposed as actions
                - ActionsLog: register of executed actions
        """
        cursor = self.db.conn.cursor()
        # cleaning database
        drop_users = """ DROP TABLE IF EXISTS Users """
        drop_sessions = """ DROP TABLE IF EXISTS Sessions """
        drop_actions = """ DROP TABLE IF EXISTS Actions """
        drop_actions_log = """ DROP TABLE IF EXISTS ActionsLog """
        cursor.execute(drop_users)
        cursor.execute(drop_sessions)
        cursor.execute(drop_actions)
        cursor.execute(drop_actions_log)
	# building database
        users = """ CREATE TABLE Users
        (Id INTEGER PRIMARY KEY,
        FullName TEXT, UserName TEXT, PassWord TEXT,
        CreateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        UpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        sessions = """ CREATE TABLE Sessions
        (Id INTEGER PRIMARY KEY,
        UserName TEXT NOT NULL, Token TEXT NOT NULL,
        StartTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        EndTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        actions = """ CREATE TABLE Actions
        (Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL, Action TEXT NOT NULL,
        CreateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        UpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        actions_log = """ CREATE TABLE ActionsLog
        (Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL, ReturnCode INT NOT NULL, RunBy TEXT,
        CreateTime DATETIME DEFAULT CURRENT_TIMESTAMP,
        UpdateTime DATETIME DEFAULT CURRENT_TIMESTAMP) """
        adding_user = """ INSERT INTO
        Users (FullName, UserName, Password)
        VALUES ('Administrator', 'root', 'root') """
        adding_action = """ INSERT INTO
        Actions (Name, Action)
        VALUES ('Test Message', 'echo "Puppy is running" > /tmp/puppy.out') """
        try:
            cursor.execute(users)
            cursor.execute(sessions)
            cursor.execute(actions)
            cursor.execute(actions_log)
            cursor.execute(adding_user)
            cursor.execute(adding_action)
            self.db.conn.commit()
            return 0
        except Exception as e:
            return e

if __name__ == "__main__":
    result = run()
    if result == 0:
        print("INFO: Successful!")
    else:
        print("ERROR:", result)
