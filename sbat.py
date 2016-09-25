#!/usr/bin/python
"""
SBAT (shitty build automation tool)

Basically, a simplistic version of gradle tasks.
"""


import sys
import taskdef
from tabulate import tabulate


def main(argv):
    """Connecting the dots between argv and taskdef.py"""
    rawtaskdefinitions = dir(taskdef)
    taskdefinitions = []

    for task in rawtaskdefinitions:
        # Remove built-in, e.g. __name__
        if not task.startswith('__'):
            taskdefinitions.append(task)

    for command in argv:
        if command == 'tasks':
            print_all_tasks(taskdefinitions)
        elif command in taskdefinitions:
            method_to_call = getattr(taskdef, command)
            result = method_to_call()
        else:
            print "\nTask '%s' isn't recognized." % command
    print "\n\nSBAT Done.\n"


def print_all_tasks(list):
    """Prints all listed tasks"""
    header = "Tasks"
    print "\n#########################################"
    print "SBAT (shitty build automation tool) tasks\n"
    print tabulate(list, header, tabulatefmt='simple') + '\n'

if __name__ == "__main__":
    main(sys.argv[1:])
