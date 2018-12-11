#!/usr/bin/python3

import unittest
from app.modules import actions

action = actions.Action("/app/modules")

class Test(unittest.TestCase):

    action_id = "1"
    name = "Create File"
    command = "touch /tmp/file.new"
    user = "ivanleoncz"

    def test01_create_action(self):
        self.assertEqual(action.create(Test.name, Test.command), "OK")

    def test02_read_action(self):
        self.assertIsInstance(action.read(Test.action_id), list)

    def test03_read_all_actions(self):
        self.assertIsInstance(action.read(), list)

    def test04_update_action(self):
        self.assertEqual(action.update(Test.action_id, Test.name,
                                                       Test.command), "OK")

    def test05_delete_action(self):
        self.assertEqual(action.delete(Test.command), "OK")

    def test06_run_action(self):
        self.assertEqual(action.run(Test.action_id, Test.user), "OK")

    def test07_history(self):
        self.assertIsInstance(action.history(), list)


if __name__ == "__main__":
    unittest.main()
