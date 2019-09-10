#!/usr/bin/python3

from pyrob.api import *
  
@task(delay=0.05)
def task_4_11():
    move_right(n=1)
    i=0
    while i!=12:
        move_down(n=1)
        for j in range(i+1):
            fill_cell()
            move_right(n=1)
        move_down(n=1)
        for j in range(i+1):
            fill_cell()
            move_left(n=1)
        fill_cell()
        i=i+2
    move_down(n=1)
    for i in range (12):
        fill_cell()
        move_right(n=1)
    fill_cell()
    move_down(n=1)
    move_left(n=12)
    
if __name__ == '__main__':
    run_tasks()