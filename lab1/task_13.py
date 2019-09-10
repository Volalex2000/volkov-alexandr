#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    while True:
        if not wall_is_above():
            move_up(n=1)
            fill_cell()
            move_down(n=1)
        if not wall_is_beneath():
            move_down(n=1)
            fill_cell()
            move_up(n=1)
        if not wall_is_on_the_right():
            move_right(n=1)
        else:
            break


if __name__ == '__main__':
    run_tasks()
