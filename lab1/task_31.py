#!/usr/bin/python3
#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.1)
def task_8_30():
    while True:
        i=0
        while not wall_is_beneath():
            move_down(n=1)
        while not wall_is_on_the_right():
            if not wall_is_beneath():
                i+=1
                break
            move_right(n=1)
        if i==1:
            continue
        while not wall_is_on_the_left():
            if not wall_is_beneath():
                i+=1
                break
            move_left(n=1)
        if i==1:
            continue
        break
            

if __name__ == '__main__':
    run_tasks()

