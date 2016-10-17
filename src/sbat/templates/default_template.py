from sbat.basetaskrunner import dependsOn
from sbat.basetaskrunner import cmd


def test():
	""" Run all tests - STUB """
	cmd("echo test task is a STUB")

def run():
	""" Run application - STUB"""
    dependsOn(test)
	cmd("echo run task is a STUB")