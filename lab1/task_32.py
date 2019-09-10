#!/us
@task(delay=0.01)
def task_8_18():
    i=0
    z=0
    while True:
        if wall_is_on_the_right():
            break
        if not wall_is_above():
            while not wall_is_above():
                move_up(n=1)
                if cell_is_filled():
                    z+=1
                else:
                    fill_cell()
                i+=1
            fill_cell()
            move_down(n=i)
            i=0
        else:
            fill_cell()
        move_right(n=1)
    mov('ax', z)
    
if __name__ == '__main__':
    run_tasks()