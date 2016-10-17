import unittest

from src.sbat.basetaskrunner import dependsOn
from src.sbat.basetaskrunner import cmd


def exampleTask():
    return 'test'


class TestBaseTaskRunner(unittest.TestCase):

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
