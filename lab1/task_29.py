#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_7():
    i=0
    while not wall_is_on_the_right():
        if cell_is_filled():
            i+=1
        if not cell_is_filled():
            i=0
        if i==3:
            break
        move_right(n=1)


if __name__ == '__main__':
    run_tasks()