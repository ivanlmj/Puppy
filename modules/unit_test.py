
import users
import unittest

user = users.User()

class Probe(unittest.TestCase):
    """ Probing functionality of multiple classes for Puppy. """
    
    def test_user_create(self):
        self.assertEqual(user.create("Captain Nemo", "nemo", "nemo2000"), 0)

    def test_user_login(self):
        self.assertEqual(user.login("nemo", "nemo2000"), 0)

    def test_user_remove(self):
        self.assertEqual(user.remove("nemo"), 0)


if __name__ == "__main__":
    unittest.main()
