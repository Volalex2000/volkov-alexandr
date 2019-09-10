#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while True:
        i=0
        while not wall_is_on_the_right():
            i+=1
            fill_cell()
            move_right(n=1)
        fill_cell()
        move_left(n=i)
        if wall_is_beneath():
            break
        else:
            move_down(n=1)

if __name__ == '__main__':
    run_tasks()
