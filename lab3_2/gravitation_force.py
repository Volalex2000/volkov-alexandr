import graphics as gr
SIZE_X = 600
SIZE_Y = 600
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

def draw_objects(coordinate[]):
    object_1 = gr.Circle(gr.Point(coord_1), 10)
    object_2 = gr.Circle(gr.Point(coord_2), 10)
    object_3 = gr.Circle(gr.Point(coord_3), 10)
    object_1.draw(window)
    object_2.draw(window)
    object_3.draw(window)

def change_coordinates(coordinate[], speed[]):
    for i in range(6, 1, 1):
        coordinate[i] = coordinate[i] + speed[i]

def change_speed(coord_1, coord_2, coord_3, speed_1, speed_2, speed_3):
    speed_1[1] = speed_1[1] + force_x_all(coord_1, coord_2, coord_3)
    speed_1[2] = speed_1[2] + force_x_all(coord_1, coord_2, coord_3)
    speed_2[1] = speed_2[1] + force_x_all(coord_2, coord_3, coord_1)
    speed_2[1] = speed_2[1] + force_y_all(coord_2, coord_3, coord_1)
    speed_3[1] = speed_3[1] + force_x_all(coord_3, coord_1, coord_2)
    speed_3[1] = speed_3[1] + force_x_all(coord_3, coord_1, coord_2)

def force_x_all(c1, c2, c3):
    return (force_x_2_objects(c1, c2) + force_x_2_objects(c1, c2))

def force_y_all(x1, y1, x2, y2, x3, y3):
    return (force_y_2_objects(x1, y1, x2, y2) + force_y_2_objects(x1, y1, x3, y3))

def force_x_2_objects(x1, y1, x2, y2):
    if x1 != x2:
        return (3500 / distance_objects(x1, y1, x2, y2)) * ((1 + (((y2 - y1) / (x2 - x1)) ** 2)) ** -0.5) * module_f(x1, x2)
    else:
        return 0

def force_y_2_objects(x1, y1, x2, y2):
    if y1 != y2:
        return (3500 / distance_objects(x1, y1, x2, y2)) * ((1 + (((x2 - x1) / (y2 - y1)) ** 2)) ** -0.5) * module_f(y1, y2)
    else:
        return 0

def distance_objects(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2

def module_f(x1, x2):
    if x1 != x2: 
        return (x2- x1) / abs(x2 - x1)
    else:
        return 0

coord_1 = [400, 400]
coord_2 = [300, 300]
coord_3 = [200, 200]
#coordinate[1] = 400 #x1 = 400
#coordinate[2] = 400 #y1 = 400
#coordinate[3] = 300 #x2 = 300
#coordinate[4] = 300 #y2 = 300
#coordinate[5] = 200 #x3 = 200
#coordinate[6] = 200 #y3 = 200

object_1 = gr.Circle(gr.Point(x1, y1), 10)
object_2 = gr.Circle(gr.Point(x2, y2), 10)
object_3 = gr.Circle(gr.Point(x3, y3), 10)
object_1.draw(window)
object_2.draw(window)
object_3.draw(window)

speed_1 = [-4, 2]
speed_2 = [0, 0]
speed_3 = [4, -2]
speed[1] = -4 #vx1 = -4
speed[2] = 2 #vy1 = 2
speed[3] = 0 #vx2 = 0
speed[4] = 0 #vy2 = 0
speed[5] = 4 #vx3 = 4
speed[6] = -2 #vy3 = -2

for i in range(1500):
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