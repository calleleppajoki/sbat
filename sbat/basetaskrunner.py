import subprocess


def dependsOn(taskToRun):
    """ Run a task before current task """
    if callable(taskToRun):
        taskToRun()
    else:
        print 'not a callable input'


def cmd(cmdToRun):
    """ Execute command """
    try:
        subprocess.call(cmdToRun, shell=True)
    except TypeError as e:
        print 'something went wrong %s' % e
