#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_down(n=1)
    move_right(n=1)
    
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

if __name__ == '__main__':
    run_tasks()
