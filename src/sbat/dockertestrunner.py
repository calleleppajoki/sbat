import subprocess


def buildDocker(appName):
    subprocess.call('docker build -t ' + appName + ' .', shell=True)


def runDockerShell(appName):
    subprocess.call('docker run -it ' + appName + ' /bin/sh -C', shell=True)
