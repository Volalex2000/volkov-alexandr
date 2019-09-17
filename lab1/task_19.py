#!/usr/bin/python3

from pyrob.api import *
    
def f1():
    while not wall_is_above():
        move_up(n=1)
        
def f2():
    while not wall_is_on_the_left():
        move_left(n=1)
        
def go():
    if not wall_is_above() and not wall_is_beneath():
            f1()
            f2()
            break
    
@task
def task_8_29():
    while not wall_is_on_the_left():
        go()
        move_left(n=1)
    while not wall_is_on_the_right():
        go()
        move_right(n=1)
        
if __name__ == '__main__':
    run_tasks()
