#!/usr/bin/python3

import datetime
import subprocess as sp
from app.modules import database


class Action:

    def __init__(self, subdir=None):
        """ Creates an instance for SQLite class.

        Parameters
            subdir : str
                defines a subdir for SQLite connector(), in order to build
                the connection URI for database path (file).

        """
        self.db = database.SQLite()
        if subdir is not None:
            self.db.subdir = subdir
        self.db.connector()


    def create(self, name, command):
        """
            Creates a new action.

            Parameters:
                - name:    action name
                - command: command that executes the action

            Returns:
                - status (str) : OK or NOK
        """
        try:
            cursor = self.db.conn.cursor()
            create_action = """ INSERT INTO Actions (Name, Action) VALUES
                                ('{0}', '{1}') """.format(name, command)
            cursor.execute(create_action)
            row_id = cursor.lastrowid
            self.db.conn.commit()
            if type(row_id) is int:
                return "OK"
            else:
                return "NOK"
        except Exception as e:
            return e


    def read(self, action_id=None):
        """
            Retrieves a list of created actions.

            Parameters:
                - action_id (opt): Id for specific action

            Returns:
                - data (list) : created actions
        """
        try:
            cursor = self.db.conn.cursor()
            data = None
            if action_id is None:
                read_actions = """ SELECT * FROM Actions """
                cursor.execute(read_actions)
                data = cursor.fetchall()
            else:
                read_actions = """ SELECT * FROM Actions
                                   WHERE Id='{0}'
                                   ORDER BY Id DESC """.format(action_id)
                cursor.execute(read_actions)
                data = cursor.fetchall()
                if len(data) > 0:
                    data = [row for row in data[0]]
            print("Read: ", data)
            self.db.conn.commit()
            return data
        except Exception as e:
            return e


    def update(self, action_id, name, command):
        """
            Updates an existent action.

            Parameters:
                - action_id: Id of the action that is going to be updated

            Returns:
                - status (str) : OK or NOK
        """
        try:
            ts = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
            cursor = self.db.conn.cursor()
            update_action = """ UPDATE Actions
                        SET Name='{0}', Action='{1}', UpdateTime='{3}'
                        WHERE Id='{2}' """.format(name, command, action_id, ts)
            cursor.execute(update_action)
            self.db.conn.commit()
            check_update = self.read(action_id)
            if check_update[3] < check_update[4]:
                return "OK"
            else:
                return "NOK"
        except Exception as e:
            return e


    def delete(self, action_id):
        """
            Deletes an action.

            Parameters:
                - action_id: Id of the Action

            Return:
                - status (str) : OK or NOK
        """
        try:
            cursor = self.db.conn.cursor()
            delete_action = """ DELETE FROM Actions
                                WHERE Id='{0}'""".format(action_id)
            cursor.execute(delete_action)
            self.db.conn.commit()
            check_delete = self.read(action_id)
            if len(check_delete) == 0:
                return "OK"
            else:
                return "NOK"
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
            run_action = """ SELECT Name, Action FROM Actions
                             WHERE Id='{0}' """.format(action_id)
            cursor.execute(run_action)
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
                create_history  = """ INSERT INTO ActionsHistory
                (Name, ReturnCode, RunBy) VALUES('{0}', '{1}', '{2}')
                """.format(action, result, user)
                cursor.execute(create_history)
                row_id = cursor.lastrowid
                self.db.conn.commit()
                if type(row_id) is int:
                    return "OK"
                else:
                    return "NOK"
            else:
                return result
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
            data = cursor.fetchall()
            self.db.conn.commit()
            return data
        except Exception as e:
            return e


