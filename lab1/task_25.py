#!/usr/bin/python3

from pyrob.api import *

def f():
    move_right(n=1)
    fill_cell()
    move_down(n=1)
    fill_cell()
    move_right(n=1)
    fill_cell()
    move_down(n=1)
    move_left(n=1)
    fill_cell()
    move_left(n=1)
    move_up(n=1)
    fill_cell()
    move_up(n=1)

@task
def task_2_2():
    move_down(n=1)
    for i in range(4):
        f()
        move_right(n=4)
    f()

if __name__ == '__main__':
    run_tasks()