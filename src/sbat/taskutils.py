import os


def dependsOn(taskToRun):
    if callable(taskToRun):
        taskToRun()
    else:
        print 'not a callable input'


def cmd(cmdToRun):
    # TODO: change to subprocess.call & split cmdToRun into list of str
    try:
        os.system(cmdToRun)
    except TypeError as e:
        print 'something went wrong %s' % e
