#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_7_5():
    move_right(n=1)
    i=1
    while True:
        fill_cell()
        for j in range(i):
            if wall_is_on_the_right():
                i=-1
                break
            move_right(n=1)
        if i==-1:
            break
        i+=1


if __name__ == '__main__':
    run_tasks()