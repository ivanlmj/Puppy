#!/usr/bin/python3

import database
import subprocess as sp

class Action:


    def __init__(self):
        self.db = database.SQLite()


    def create(self, name, action):
        """
            Creates a new action.

            Parameters:
                - name:   action name
                - action: command that executes the action
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ INSERT INTO Actions (Name, Action) VALUES
                        ('{0}', '{1}') """.format(name, action)
            cursor.execute(query)
            self.db.conn.commit()
            return 0
        except Exception as e:
            return e


    def run(self, action_id, user):
        """
            Runs an action, based on action_id.

            Parameters:
                - action_id: action_id for running a specfic action
        """
        try:
            cursor = self.db.conn.cursor()
            query_action = """ SELECT Name, Action FROM Actions
                               WHERE Id='{0}'""".format(action_id)
            cursor.execute(query_action)
            action_data = cursor.fetchall()[0]
            self.db.conn.commit()
            action  = action_data[0]
            command = action_data[1]
            result  = sp.call(command.split())
            if result == 0:
                query_action_log  = """ INSERT INTO ActionsLog
                (Name, ReturnCode, RunBy) VALUES('{0}', '{1}', '{2}')
                """.format(action, result, user)
                cursor.execute(query_action_log)
                self.db.conn.commit()
                return 0
            else:
                return 1
        except Exception as e:
            return e


    def show(self, action_id=None):
        """
         Shows actions as JSON document.

            Parameters:
                - action_id (optional): action_id for retrieving specific data
        """
        try:
            cursor = self.db.conn.cursor()
            query = None
            if action_id is None:
                query = """ SELECT * FROM Actions """
            else:
                query = """ SELECT * FROM Actions
                            WHERE Id='{0}'""".format(action_id)
            cursor.execute(query)
            data = [ row for row in cursor.fetchall() ]
            self.db.conn.commit()
            return data
        except Exception as e:
            return e


    def logged(self):
        """
            List logged actions.
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ SELECT * FROM ActionsLog """
            cursor.execute(query)
            data = cursor.fetchall()
            self.db.conn.commit()
            return data
        except Exception as e:
            return e


    def remove(self, name):
        """
            Removes an action.

            Parameters:
                - name:   action name
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ DELETE FROM Actions WHERE Name='{0}'""".format(name)
            cursor.execute(query)
            self.db.conn.commit()
            query_remove = """ SELECT * FROM Actions
                               WHERE Name='{0}'""".format(name)
            cursor.execute(query_remove)
            data = cursor.fetchall()
            if len(data) == 0:
                return 0
            else:
                return 1
        except Exception as e:
            return e
