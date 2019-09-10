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

def g():
    for i in range(9):
        f()
        move_right(n=4)
    f()
    move_left(n=36)
    
@task(delay=0.01)
def task_2_4():
    for j in range (4):
        g()
        move_down(n=4)
    g()
    
if __name__ == '__main__':
    run_tasks()