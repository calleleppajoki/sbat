from sbat.basetaskrunner import dependsOn
from sbat.basetaskrunner import cmd
from sbat.dockertestrunner import buildDocker
from sbat.dockertestrunner import runDockerShell


APPNAME = 'sbat'


def hello():
    """example task that echoes hello world"""
    cmd('echo hello world')


def test():
    """Test runs all unit tests"""
    print 'RUN ALL TESTS - FROM TASKDEF'


def testbefore():
    """TODO: Until unittest is added - keep test here"""
    print 'Run first'


def testDependsOn():
    """TODO: Until unittest is added - keep test here"""
    dependsOn(testbefore)
    print 'Run after dependsOn'


def dockerBuild():
    """ Build from Dockerfile """
    buildDocker(APPNAME)


def dockerShell():
    """ Start container and open shell """
    runDockerShell(APPNAME)
