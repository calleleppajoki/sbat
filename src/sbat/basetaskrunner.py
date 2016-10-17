import subprocess


def dependsOn(taskToRun):
    if callable(taskToRun):
        taskToRun()
    else:
        print 'not a callable input'


def cmd(cmdToRun):
    try:
        subprocess.call(cmdToRun, shell=True)
    except TypeError as e:
        print 'something went wrong %s' % e
