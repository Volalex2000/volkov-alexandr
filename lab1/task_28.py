#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_6():
    i=0
    while True:
        if cell_is_filled():
            i+=1
        if i==5:
            break
        move_right(n=1)


if __name__ == '__main__':
    run_tasks()
