#!/usr/bin/python3

import database
import subprocess as sp

class Actions:


    def __init__(self):
        self.db = database.SQLite()


    def run_action(self, action_id, user):
        """
            Runs an action, based on action_id.

            Parameters:
                - action_id: action_id for running a specfic action
        """
        cursor = self.db.conn.cursor()
        query_action = """ SELECT Name, Action FROM Actions
                           WHERE Id='{0}'""".format(action_id)
        cursor.execute(query_action)
        action_data   = cursor.fetchall()
        action_name   = action_data[0]
        action_result = sp.call(action_data[1])
        if action_result == 0:
            query_action_log  = """ INSERT INTO ActionsLog
            (Name, ReturnCode, RunBy) VALUES
            ('{0}', '{1}', '{2}')""".format(action_name, action_result, User)
            cursor.execute(query_action_log)
        self.db.conn.commit()
        return action_result


    def create_action(self, name, action):
        """
            Creates a new action.

            Parameters:
                - name:   action name
                - action: command that executes the action
        """
        cursor = self.db.conn.cursor()
        query = """ INSERT INTO Actions (Name, Action) VALUES
                    ('{0}', '{1}') """.format(name, action)
        cursor.execute(query)
        self.db.conn.commit()


    def remove_action(self, name):
        """
            Removes an action.

            Parameters:
                - name:   action name
        """
        cursor = self.db.conn.cursor()
        query = """ DELETE FROM Actions WHERE Name='{0}'""".format(name)
        cursor.execute(query)
        self.db.conn.commit()


    def list_actions(self, action_id=None):
        """
            List actions.

            Parameters:
                - action_id (optional): action_id for retrieving specific data
        """
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


    def logged_actions(self):
        """
            List logged actions.
        """
        cursor = self.db.conn.cursor()
        query = """ SELECT * FROM ActionsLog """
        cursor.execute(query)
        data = cursor.fetchall()
        self.db.conn.commit()
        return data
