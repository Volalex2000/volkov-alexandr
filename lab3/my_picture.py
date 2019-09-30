import graphics as gr
w = gr.GraphWin("My picture", 1000, 1000)

z=gr.Rectangle(gr.Point(0, 500), gr.Point(1000, 1000))
z.setFill('green')
z.draw(w)
for i in range(50,1000,50):
    tr=gr.Line(gr.Point(i, 400), gr.Point(i+50, 500))
    tr.setOutline('green')
    tr.draw(w)
for i in range(100,1000,200):
    for j in range (600,1000,200):
        tsl1=gr.Circle(gr.Point(i-30, j-30), 50)
        tsl1.setFill('white')
        tsl1.draw(w)
        tsl2=gr.Circle(gr.Point(i-30, j+30), 50)
        tsl2.setFill('white')
        tsl2.draw(w)
        tsl3=gr.Circle(gr.Point(i+30, j-30), 50)
        tsl3.setFill('white')
        tsl3.draw(w)
        tsl4=gr.Circle(gr.Point(i+30, j+30), 50)
        tsl4.setFill('white')
        tsl4.draw(w)
        tsc=gr.Circle(gr.Point(i, j), 50)
        tsl4.setFill('yellow')
        tsc.draw(w)
d1=gr.Rectangle(gr.Point(300, 400), gr.Point(400, 800))
d1.setFill('brown') 
d1.draw(w)
for i in range(200,600,100):
    for j in range (100,500,100):
        d2=gr.Circle(gr.Point(i, j), 150)
        d2.setFill("#00a0a0")
        d2.draw(w)   
chl=gr.Polygon(gr.Point(650, 300),gr.Point(750, 400),gr.Point(650, 300))
chl.setWidth(30)
w.getMouse()
w.close()
