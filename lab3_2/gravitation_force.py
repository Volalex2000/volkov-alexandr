import graphics as gr
SIZE_X = 600
SIZE_Y = 600
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

def draw_objects(coord_1, coord_2, coord_3):
    object_1 = gr.Circle(gr.Point(coord_1), 10)
    object_2 = gr.Circle(gr.Point(coord_2), 10)
    object_3 = gr.Circle(gr.Point(coord_3), 10)
    object_1.draw(window)
    object_2.draw(window)
    object_3.draw(window)

def change_coordinates(coordinate, speed):
    for i in range(2):
        coord_1[i] = coord_1[i] + speed_1[i]
        coord_2[i] = coord_2[i] + speed_2[i]
        coord_3[i] = coord_3[i] + speed_3[i]

def change_speed(coord_1, coord_2, coord_3, speed_1, speed_2, speed_3):
    speed_1[0] = speed_1[0] + force_x_all(coord_1, coord_2, coord_3)
    speed_1[1] = speed_1[1] + force_y_all(coord_1, coord_2, coord_3)
    speed_2[0] = speed_2[0] + force_x_all(coord_2, coord_3, coord_1)
    speed_2[1] = speed_2[1] + force_y_all(coord_2, coord_3, coord_1)
    speed_3[0] = speed_3[0] + force_x_all(coord_3, coord_1, coord_2)
    speed_3[1] = speed_3[1] + force_y_all(coord_3, coord_1, coord_2)

def force_x_all(c1, c2, c3):
    return (force_x_2_objects(c1, c2) + force_x_2_objects(c1, c3))

def force_y_all(c1, c2, c3):
    return (force_y_2_objects(c1, c2) + force_y_2_objects(c1, c3))

def force_x_2_objects(c1, c2):
    if c1[0] != c2[0]:
        return (3500 / distance_objects(x1, y1, x2, y2)) * ((1 + (((c2[1] - c1[1]) / (c2[0] - c1[0])) ** 2)) ** -0.5) * module_f(c1[0], c2[0])
    else:
        return 0

def force_y_2_objects(c1, c2):
    if c1[1] != c2[1]:
        return (3500 / distance_objects(x1, y1, x2, y2)) * ((1 + (((c2[0] - c1[0]) / (c2[1] - c1[1])) ** 2)) ** -0.5) * module_f(c1[1], c2[1])
    else:
        return 0

def distance_objects(c1, c2):
    return (c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2

def module_f(d1, d2):
    if x1 != x2: 
        return (d2- d1) / abs(d2 - d1)
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

object_1 = gr.Circle(gr.Point(coord_1[0], coord_1[1]), 10)
object_2 = gr.Circle(gr.Point(coord_2[0], coord_2[1]), 10)
object_3 = gr.Circle(gr.Point(coord_3[0], coord_3[1]), 10)
object_1.draw(window)
object_2.draw(window)
object_3.draw(window)

speed_1 = [-4, 2]
speed_2 = [0, 0]
speed_3 = [4, -2]
#speed[1] = -4 vx1 = -4
#speed[2] = 2 vy1 = 2
#speed[3] = 0 vx2 = 0
#speed[4] = 0 vy2 = 0
#speed[5] = 4 vx3 = 4
#speed[6] = -2 vy3 = -2

for i in range(1500):
    change_coordinates()

    object_1.move(speed_1)
    object_2.move(speed_2)
    object_3.move(speed_3)

    drow_coordinates_1 = gr.Point(coord_1)
    drow_coordinates_2 = gr.Point(coord_2)
    drow_coordinates_3 = gr.Point(coord_3)
    drow_coordinates_1.draw(window)
    drow_coordinates_2.draw(window)
    drow_coordinates_3.draw(window)

    change_speed()
    gr.time.sleep(0.1)
    
window.getMouse()
window.close()