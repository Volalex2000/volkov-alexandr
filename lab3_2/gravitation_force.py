import graphics as gr
SIZE_X = 400
SIZE_Y = 400
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

def change_coordinates():
    pass

def force():
    pass

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
    x1=100
    y1=100
    x2=300
    y2=300
    x3=200
    y3=200
    draw_objects(x1, y1, x2, y2, x3, y3)

main()
window.getMouse()
window.close()