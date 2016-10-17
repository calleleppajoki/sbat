from sbat.basetaskrunner import dependsOn
from sbat.basetaskrunner import cmd


def test():
	""" Run all tests """
	cmd("pytest")

def style():
    """ Run flake8 """