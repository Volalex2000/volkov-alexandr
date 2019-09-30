import graphics as gr

SIZE_X = 400
SIZE_Y = 400

window1 = gr.GraphWin("Model", SIZE_X, SIZE_Y)

x1=200
y1=100
x2=200
y2=300

c1 = gr.Circle(gr.Point(x1, y1), 10)
c2 = gr.Circle(gr.Point(x2, y2), 10)
c1.draw(window1)
c2.draw(window1)

v1x=5
v1y=0
v2x=-5
v2y=0

for i in range(300):
    
    r2=(x1-x2)**2+(y1-y2)**2

    if x2!=x1:
        zn1=(x2-x1)/abs(x2-x1)
        Fx=(10000/r2)*((1+(((y2-y1)/(x2-x1))**2))**-0.5)*zn1
    else:
        Fx=0
    if y2!=y1:
        zn2=(y2-y1)/abs(y2-y1)
        Fy=(10000/r2)*(1/(1+((x2-x1)/(y2-y1))**2)**0.5)*zn2
    else:
        Fy=0
    
    v1x += Fx
    v2x -= Fx
    v1y += Fy
    v2y -= Fy
    
    x1=x1+v1x
    x2=x2+v2x
    y1=y1+v1y
    y2=y2+v2y
    
    t1=gr.Point(x1, y1)
    t2=gr.Point(x2, y2)
    t1.draw(window1)
    t2.draw(window1)
    
    c1.move(v1x, v1y)
    c2.move(v2x, v2y)
    
    gr.time.sleep(0.05)

window1.getMouse()

window1.close()