#!/usr/bin/python3

from pyrob.api import *

def kr(a,b,c):
    if a!=b and a!=c:
            fill_cell()

@task(delay=0.01)              
def task_9_3():
    h=0
    while not wall_is_on_the_right():
        h+=1
        move_right(n=1)
    move_left(n=h)
    
    for i in range(h):
        for j in range(h):
            kr(j, h-i, i)
            move_right(n=1)
        kr(j+1, h-i, i)
        move_left(n=h)
        move_down(n=1)
    for j in range(h):
        kr(j, h-i-1, i+1)
        move_right(n=1)
    kr(j+1, h-i-1, i+1)
    move_left(n=h)
          
if __name__ == '__main__':
    run_tasks()
