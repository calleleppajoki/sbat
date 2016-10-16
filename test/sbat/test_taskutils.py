import unittest

from src.sbat.taskutils import dependsOn
from src.sbat.taskutils import cmd


def exampleTask():
    return 'test'


class TestTaskUtils(unittest.TestCase):

    def test_dependsOnCallable(self):
        """ Expect None when it's working """
        self.assertIsNone(dependsOn(exampleTask), 'test')

    def test_dependsOnNotCallable(self):
        self.assertRaises(TypeError, dependsOn(0))

    def test_cmdCallable(self):
        """ Expect None when it's working """
        self.assertIsNone(cmd('ls'))

    def test_cmdNotCallable(self):
        self.assertRaises(TypeError, cmd(0))


if __name__ == '__main__':
    unittest.main()
