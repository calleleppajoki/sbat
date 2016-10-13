import os
from sbat import dependsOn
"""Add tasks by creating a function."""


def hello():
    """example task that echoes hello world"""
    os.system('echo hello world')


def test():
    """Test runs all unit tests"""
    print "RUN ALL TESTS - FROM TASKDEF"


def testbefore():
    """TODO: Until unittest is added - keep test here"""
    print "Run first"


def testDependsOn():
    """TODO: Until unittest is added - keep test here"""
    dependsOn(testbefore)
    print "Run after dependsOn"
