#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_1():
    move_right(n=2)
    move_down(n=3)
    move_right(n=2)


if __name__ == '__main__':
    run_tasks()
