import os

def dependsOn(taskToRun):
    taskToRun()

def cmd(cmdToRun):
    os.system(cmdToRun)
