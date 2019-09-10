#!/usr/bin/python3

from pyrob.api import *
       
@task(delay=0.01)
                   
def task_9_3():
    h=0
    while not wall_is_on_the_right():
        h+=1
        move_right(n=1)
    move_left(n=h)
    
    for i in range(h):
        for j in range(h):
            if j!=h-i and j!=i:
                fill_cell()
            move_right(n=1)
        if j+1!=h-i and j+1!=i:
            fill_cell()
        move_left(n=h)
        move_down(n=1)
    for j in range(h):
        if j!=h-1-i and j!=i+1:
            fill_cell()
        move_right(n=1)
    if j+1!=h-1-i and j+1!=i+1:
        fill_cell()
    move_left(n=h)
          
if __name__ == '__main__':
    run_tasks()