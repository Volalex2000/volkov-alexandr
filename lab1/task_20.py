#!/usr/bin/python3

from pyrob.api import *
  
@task(delay=0.05)
def task_4_3():
    move_right(n=1)
    for i in range(7):
        for j in range(27):
            fill_cell()
            move_right(n=1)
        move_down(n=1)
        for j in range(27):
            fill_cell()
            move_left(n=1)
        move_down(n=1)

if __name__ == '__main__':
    run_tasks()
