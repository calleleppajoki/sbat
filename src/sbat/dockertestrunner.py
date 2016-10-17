import subprocess


def dockerBuild(appName):
    subprocess.call('docker build -t ' + appName + ' .', shell=True)


def dockerShell(appName):
    subprocess.call('docker run -it ' + appName + ' /bin/sh -C', shell=True)
