#!/usr/bin/python3

from pyrob.api import *

@task(delay=0.01)
def task_6_6():
    i=0
    j=0
    move_right(n=1)
    while True:
        if not wall_is_above():
            while not wall_is_above():
                move_up(n=1)
                i+=1
                fill_cell()
            move_down(n=i)
            i=0
        if wall_is_on_the_right():
            break
        move_right(n=1)
        j+=1
    move_left(n=j+1)


if __name__ == '__main__':
    run_tasks()
