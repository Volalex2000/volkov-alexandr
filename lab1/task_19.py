#!/usr/bin/python3

from pyrob.api import *
    
def f1():
    while not wall_is_above():
        move_up(n=1)
        
def f2():
    while not wall_is_on_the_left():
        move_left(n=1)

@task
def task_8_29():
    i=0
    while wall_is_above():
        if wall_is_on_the_left():
            i=1
            move_right(n=1)
        if i==0:
            move_left(n=1)
        elif not wall_is_on_the_right():
            move_right(n=1)
        else:
            break
    else:
        f1()
        f2()
if __name__ == '__main__':
    run_tasks()
