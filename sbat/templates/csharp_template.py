from sbat.basetaskrunner import dependsOn # noqa F841
from sbat.basetaskrunner import cmd # noqa F841


def restore():
    """dotnet restore"""
    cmd('dotnet restore')


def dotnetrun():
    """dotnet run"""
    dependsOn(publish)
    cmd('dotnet run')


def publish():
    """dotnet publish"""
    cmd('dotnet publish')


def build():
    """docker build"""
    cmd('docker build -t testapp .')


def run():
    """docker run"""
    cmd('docker run -it -p 5000:5000 testapp')
