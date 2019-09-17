#!/usr/bin/python3

from pyrob.api import *
    
def f1():
    while not wall_is_above():
        move_up(n=1)
        
def f2():
    while not wall_is_on_the_left():
        move_left(n=1)
    
def pr(n):
    if not wall_is_above():
        move_up(n=1)
        break  
    else:
        if n==0:
            move_left(n=1)
        else:
            move_right(n=1)

    
    
@task
def task_8_28():
    while not wall_is_on_the_left():
        pr(0)   
    while not wall_is_on_the_right():
        pr(1)
    f1()
    f2()
        
if __name__ == '__main__':
    run_tasks()
