#import pytest
import unittest
from mock import MagicMock

from src.sbat.taskutils import dependsOn
from src.sbat.taskutils import cmd

from src.taskdef import hello

class TestTaskUtils(unittest.TestCase):

    def test_dependsOnPositive(self):
        #mock.exampletask = "hello world"
        #thing = ProductionClass()
        #thing.method = MagicMock(return_value=3)
        self.assertEqual( dependsOn(exampleTask), 'test' )

    def test_cmdPositive(self):
        self.assertEqual( cmd('echo "hello world"'), 'hello world' )

if __name__ == '__main__':
    unittest.main()