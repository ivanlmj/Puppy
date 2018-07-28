#!/usr/bin/python3

""" Module defined for testing multiple aspects from Puppy modules. """

import users
import unittest

user = users.User()

class Probe(unittest.TestCase):
    """ Probing functionalities from Puppy. """
    
    def test_user_create(self):
        """ Testing user ceation. """
        self.assertEqual(user.create("Captain Nemo", "nemo", "nemo2000"), 0)

    def test_user_login(self):
        """ Testing user login. """
        self.assertEqual(user.login("nemo", "nemo2000"), 0)

    def test_user_remove(self):
        """ Testing user removal. """
        self.assertEqual(user.remove("nemo"), 0)


if __name__ == "__main__":
    unittest.main()
