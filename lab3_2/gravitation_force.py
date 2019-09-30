import graphics as gr
SIZE_X = 400
SIZE_Y = 400
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

def change_coordinates():
    pass

def force(x1, y1, x2, y2, x3, y3):
    distance_objects_1_2 = (x1-x2)**2+(y1-y2)**2
    distance_objects_2_3 = (x2-x3)**2+(y2-y3)**2
    distance_objects_2_3 = (x3-x1)**2+(y3-y1)**2

    module_fx12 = (x2-x1)/abs(x2-x1)
    module_fy12 = (y2-y1)/abs(y2-y1)
    module_fx23 = (x2-x1)/abs(x2-x1)
    module_fy23 = (y2-y1)/abs(y2-y1)
    module_fx31 = (x2-x1)/abs(x2-x1)
    module_fy31 = (y2-y1)/abs(y2-y1)


def change_speed():
    pass

def draw_objects(x1, y1, x2, y2, x3, y3):
    object_1 = gr.Circle(gr.Point(x1, y1), 10)
    object_2 = gr.Circle(gr.Point(x2, y2), 10)
    object_3 = gr.Circle(gr.Point(x3, y3), 10)
    object_1.draw(window)
    object_2.draw(window)
    object_3.draw(window)

def main():
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

    force(x1, y1, x2, y2, x3, y3)
    change_speed()
    change_coordinates
    
main()
window.getMouse()
window.close()