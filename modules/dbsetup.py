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
        users_admin = """ INSERT INTO
        Users (FullName, UserName, Password)
        VALUES ('Administrator', 'root', 'root') """
        cursor.execute(users)
        cursor.execute(sessions)
        cursor.execute(actions)
        cursor.execute(actions_log)
        cursor.execute(users_admin)
        self.db.conn.commit()
        print("Done!")
