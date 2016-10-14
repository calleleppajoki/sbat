import pytest
import unittest

from src.taskutils import dependsOn
from src.taskutils import cmd

class TestDependsOn(unittest.TestCase):
    def exampleTask():
        print 'test'

    def test_dependsOnPositive(self):
        self.assertEqual( dependsOn(exampleTask), 'test' )

class TestCmd:
    def test_cmdPositive(self):
        self.assertEqual( cmd('echo "hello world"'), 'hello world' )