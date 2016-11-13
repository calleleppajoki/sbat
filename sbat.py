#!/usr/bin/python
"""
SBAT (simple/shitty build automation tool)

Basically, a simplistic version of gradle tasks.
"""


import sys
import taskdef
from tabulate import tabulate


def main(argv):
    rawtaskdefinitions = dir(taskdef)
    taskdefinitions = []
    taskdefinitionsbeautified = []
    excludeFilter = ('__', 'cmd', 'dependsOn', 'APPNAME')

    for task in rawtaskdefinitions:
        # Remove built-in, e.g. __name__
        if not task.startswith(excludeFilter):
            doc = getattr(taskdef, task).__doc__
            taskdefinitions.append(task)
            taskdefinitionsbeautified.append([task, doc])
    
    for command in argv:
        if command == 'tasks':
            print_all_tasks(taskdefinitionsbeautified)
        elif command in taskdefinitions:
            method_to_call = getattr(taskdef, command)
            result = method_to_call() # noqa F841
        else:
            print "\nTask '%s' isn't recognized." % command
    print "\n\nSBAT Done.\n"


def print_all_tasks(tasks):
    header = ["Tasks", "Desc"]
    print "\n################################################"
    print "SBAT (simple/shitty build automation tool) tasks\n"
    print tabulate(tasks, header, tablefmt='simple') + '\n'


if __name__ == "__main__":
    main(sys.argv[1:])
