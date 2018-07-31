#!/usr/bin/python3

""" Module defined for testing multiple aspects from Puppy modules. """

import actions
import users
import unittest

action = actions.Action()
user = users.User()

class Probe(unittest.TestCase):
    """ Probing functionalities from Puppy. """
    
    # User() class test
    def test_user_create(self):
        """ Testing user ceation. """
        self.assertEqual(user.create("Captain Nemo", "nemo", "nemo2000"), 0)

    def test_user_login(self):
        """ Testing user login. """
        self.assertEqual(user.login("nemo", "nemo2000"), 0)

    def test_user_remove(self):
        """ Testing user removal. """
        self.assertEqual(user.remove("nemo"), 0)

    # Action() class test
    def test_action_create(self):
        """ Testing action creation. """
        self.assertEqual(action.create("Create File", "touch /tmp/file"), 0)

    def test_action_run(self):
        """ Testing action execution. """
        self.assertEqual(action.run(0, "root"), 0)

    def test_action_show(self):
        """ Testing display of actions. """
        self.assertEqual(type(action.show()), list)

    def test_action_logged(self):
        """ Testing display of logged actions. """
        self.assertEqual(type(action.logged()), list)

    def test_action_remove(self):
        """ Testing action removal. """
        self.assertEqual(action.remove(), 0)

if __name__ == "__main__":
    unittest.main()
