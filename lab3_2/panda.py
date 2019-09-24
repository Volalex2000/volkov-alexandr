import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

def stalk():
    pass

def leaf():
    pass

def tree():
    stalk()
    leaf()
    pass

def panda():
    pass

def main():
    background=gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
    background.setFill('#FF9999')
    background.draw(window)
    
    panda()
    tree()

main()
window.getMouse()
window.close()