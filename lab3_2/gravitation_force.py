import graphics as gr
SIZE_X = 600
SIZE_Y = 600
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

def draw_objects(x1, y1, x2, y2, x3, y3):
    object_1 = gr.Circle(gr.Point(x1, y1), 10)
    object_2 = gr.Circle(gr.Point(x2, y2), 10)
    object_3 = gr.Circle(gr.Point(x3, y3), 10)
    object_1.draw(window)
    object_2.draw(window)
    object_3.draw(window)

def change_coordinates():
    global x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3
    x1 = x1 + vx1
    y1 = y1 + vy1
    x2 = x2 + vx2
    y2 = y2 + vy2
    x3 = x3 + vx3
    y3 = y3 + vy3

def change_speed():
    global x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3
    vx1 = vx1 + force_x_all(x1, y1, x2, y2, x3, y3)
    vy1 = vy1 + force_y_all(x1, y1, x2, y2, x3, y3)
    vx2 = vx2 + force_x_all(x2, y2, x3, y3, x1, y1)
    vy2 = vy2 + force_y_all(x2, y2, x3, y3, x1, y1)
    vx3 = vx3 + force_x_all(x3, y3, x1, y1, x2, y2)
    vy3 = vy3 + force_y_all(x3, y3, x1, y1, x2, y2)

def force_x_all(x1, y1, x2, y2, x3, y3):
    return (force_x_2_objects(x1, y1, x2, y2) + force_x_2_objects(x1, y1, x3, y3))

def force_y_all(x1, y1, x2, y2, x3, y3):
    return (force_y_2_objects(x1, y1, x2, y2) + force_y_2_objects(x1, y1, x3, y3))

def force_x_2_objects(x1, y1, x2, y2):
    if x1 != x2:
        return (1000 / distance_objects(x1, y1, x2, y2)) * ((1 + (((y2 - y1) / (x2 - x1)) ** 2)) ** -0.5) * module_f(x1, x2)
    else:
        return 0

def force_y_2_objects(x1, y1, x2, y2):
    if y1 != y2:
        return (1000 / distance_objects(x1, y1, x2, y2)) * ((1 + (((x2 - x1) / (y2 - y1)) ** 2)) ** -0.5) * module_f(y1, y2)
    else:
        return 0

def distance_objects(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def module_f(x1, x2):
    if x1 != x2: 
        return (x2- x1) / abs(x2 - x1)
    else:
        return 0


x1 = 400
y1 = 400
x2 = 300
y2 = 300
x3 = 200
y3 = 200

object_1 = gr.Circle(gr.Point(x1, y1), 10)
object_2 = gr.Circle(gr.Point(x2, y2), 10)
object_3 = gr.Circle(gr.Point(x3, y3), 10)
object_1.draw(window)
object_2.draw(window)
object_3.draw(window)

vx1 = -3
vy1 = -2
vx2 = 2
vy2 = -2
vx3 = 3
vy3 = 2

for i in range(1000):
    change_coordinates()

    object_1.move(vx1, vy1)
    object_2.move(vx2, vy2)
    object_3.move(vx3, vy3)

    drow_coordinates_1 = gr.Point(x1, y1)
    drow_coordinates_2 = gr.Point(x2, y2)
    drow_coordinates_3 = gr.Point(x3, y3)
    drow_coordinates_1.draw(window)
    drow_coordinates_2.draw(window)
    drow_coordinates_3.draw(window)

    change_speed()
    gr.time.sleep(0.1)
    
window.getMouse()
window.close()