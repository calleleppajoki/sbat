import subprocess


def buildDocker(appName):
    """ Build docker container """
    subprocess.call('docker build -t ' + appName + ' .', shell=True)


def runDockerShell(appName):
    """ Run container with interactive shell """
    subprocess.call('docker run -it ' + appName + ' /bin/sh -C', shell=True)


def runDockerCommand(appName, command):
    """ Run container and command defined in docker-entrypoint.sh """
    subprocess.call('docker run --rm -i ' + appName + ' ' + command, shell=True)
