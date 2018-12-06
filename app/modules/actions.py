#!/usr/bin/python3

import subprocess as sp
from app.modules import database


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


    def update(self, action_id, name, action):
        """
            Updates an existent action.

            Parameters:
                - action_id: Id of the action that is going to be updated
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ UPDATE Actions SET Name={0}, Action={1}
                        WHERE Id={2}""".format(name, action, action_id)
            cursor.execute(query)
            self.db.conn.commit()
            return 0
        except Exception as e:
            return e


    def delete(self, action_id):
        """
            Removes an action.

            Parameters:
                - action_id: Id of the Action

            Return:
                - 0: action removed
                - 1: action not removed
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ DELETE FROM Actions WHERE Id='{0}'""".format(name)
            cursor.execute(query)
            self.db.conn.commit()
            check_remove = """ SELECT * FROM Actions
                               WHERE Id='{0}'""".format(name)
            cursor.execute(check_remove)
            data = cursor.fetchall()
            self.db.conn.commit()
            if len(data) == 0:
                return 0
            else:
                return 1
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
            # TODO:
            #
            # 1 - expand env variables: os.path.expand(command)
            # 2 - sanitize command for cases like "rm -rf /"
            result  = sp.call(command.split())
            if result == 0:
                query_action_log  = """ INSERT INTO ActionsHistory
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
            Lists created actions (depending on optional parameter).

            Parameters:
                - action_id (opt): Id for specific action

            Return:
                - list : created actions
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


    def history(self):
        """
            Lists executed actions.

            Return:
                - list : executed actions
        """
        try:
            cursor = self.db.conn.cursor()
            query = """ SELECT * FROM ActionsHistory """
            cursor.execute(query)
            data = [ row for row in cursor.fetchall() ]
            self.db.conn.commit()
            return data
        except Exception as e:
            return e


