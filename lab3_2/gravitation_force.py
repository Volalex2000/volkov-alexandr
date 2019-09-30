import graphics as gr
SIZE_X = 400
SIZE_Y = 400
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

def change_coordinates(vx1, vy1, vx2, vy2, vx3, vy3):
    global x1
    global y1
    global x2
    global y2
    global x3
    global y3
    x1 = x1 + vx1
    y1 = y1 + vy1
    x2 = x2 + vx2
    y2 = y2 + vy2
    x3 = x3 + vx3
    y3 = y3 + vy3
    print("A")

def force_x_2_objects(x1, y1, x2, y2):
    if module_f(x1, x2) != 0:
        return (10000 / distance_objects(x1, y1, x2, y2)) * ((1 + (((y2 - y1) / (x2 - x1)) ** 2)) ** -0.5)*module_f(x1, x2)
    else:
        return 0
    print("b")

def force_y_2_objects(x1, y1, x2, y2):
    if module_f(y1, y2) != 0:
        return (10000 / distance_objects(x1, y1, x2, y2)) * ((1 + (((x2 - x1) / (y2 - y1)) ** 2)) ** -0.5)*module_f(y1, y2)
    else:
        return 0
    print("c")

def force_x_all(x1, y1, x2, y2, x3, y3):
    return force_y_2_objects(x1, y1, x2, y2) + force_y_2_objects(x1, y1, x3, y3)

def force_y_all(x1, y1, x2, y2, x3, y3):
    return force_y_2_objects(x1, y1, x2, y2) + force_y_2_objects(x1, y1, x3, y3)

def distance_objects(x1, y1, x2, y2):
    return (x1-x2)**2+(y1-y2)**2

def module_f(x1, x2):
    if x1 != x2: 
        return (x2-x1)/abs(x2-x1)
    else:
        return 0

def change_speed(x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3):
    vx1 = vx1 + force_x_all(x1, y1, x2, y2, x3, y3)
    vy1 = vy1 + force_y_all(x1, y1, x2, y2, x3, y3)
    vx2 = vx2 + force_x_all(x2, y2, x3, y3, x1, y1)
    vy2 = vy2 + force_y_all(x2, y2, x3, y3, x2, y2)
    vx3 = vx3 + force_x_all(x3, y3, x1, y1, x2, y2)
    vy3 = vy3 + force_y_all(x3, y3, x1, y1, x2, y2)

def draw_objects(x1, y1, x2, y2, x3, y3):
    object_1 = gr.Circle(gr.Point(x1, y1), 10)
    object_2 = gr.Circle(gr.Point(x2, y2), 10)
    object_3 = gr.Circle(gr.Point(x3, y3), 10)
    object_1.draw(window)
    object_2.draw(window)
    object_3.draw(window)

x1 = 100
y1 = 100
x2 = 300
y2 = 300
x3 = 200
y3 = 200
draw_objects(x1, y1, x2, y2, x3, y3)

vx1 = 5
vy1 = 0
vx2 = -5
vy2 = 0
vx3 = 5
vy3 = -5

for i in range(30):
    change_coordinates(vx1, vy1, vx2, vy2, vx3, vy3)
    draw_objects(x1, y1, x2, y2, x3, y3)
    change_speed(x1, y1, x2, y2, x3, y3, vx1, vy1, vx2, vy2, vx3, vy3)
    print(x1)
    print(y1)
    
window.getMouse()
window.close()