from sbat.basetaskrunner import dependsOn # noqa F841
from sbat.basetaskrunner import cmd  # noqa F841


def test():
    """ Run all tests """
    dependsOn(style)
    cmd('pytest')


def style():
    """ Run flake8 """
    cmd('flake8')
