from sbat.basetaskrunner import dependsOn
from sbat.basetaskrunner import cmd


def test():
    """ Run all tests """
    dependsOn(style)
    cmd('pytest')


def style():
    """ Run flake8 """
    cmd('flake8')
