import graphics as gr
import random

w = 800
h = 600


def cloud(w1, h1, r):
    circle1 = gr.Circle(gr.Point(w1, h1), r)#круги отдалил друг от друга и их увеличил
    circle2 = gr.Circle(gr.Point(w1 + r+10, h1), r)
    circle3 = gr.Circle(gr.Point(w1 +3 * r / 2, h1 + r / 2), r)
    circle4 = gr.Circle(gr.Point(w1 + r / 2, h1 + r / 2), r)
    circle5 = gr.Circle(gr.Point(w1 - r / 2, h1 + r / 2), r)
    circle1.setFill('#a0a0a0')#сделал другой цвет облакам
    circle2.setFill('#a0a0a0')
    circle3.setFill('white')
    circle4.setFill('#a0a0a0')
    circle5.setFill('white')
    circle1.draw(window)
    circle2.draw(window)
    circle3.draw(window)
    circle4.draw(window)
    circle5.draw(window)


def wheel(cx, cy, r1, r2):
    circle1 = gr.Circle(gr.Point(cx, cy), r2)
    circle1.setFill('black')
    circle2 = gr.Circle(gr.Point(cx, cy), r1)
    circle2.setFill('gray')
    circle1.draw(window)
    circle2.draw(window)

def House(a):
    for i in range(2):#сделал 2 этажа
        house1 = gr.Rectangle(gr.Point(20+200*a, 150+100*i), gr.Point(120+200*a, 250+100*i))
        house1.setFill('gray')
        house1.draw(window)
    
        wind = gr.Rectangle(gr.Point(45+200*a, 175+100*i), gr.Point(95+200*a, 225+100*i))#окна расширил
        wind.setFill('yellow')
        wind.draw(window)

        wline1 = gr.Line(gr.Point(70+200*a, 175+100*i), gr.Point(70+200*a, 225+100*i))
        wline1.setWidth(3)
        wline1.draw(window)

        wline2 = gr.Line(gr.Point(45+200*a, 200+100*i), gr.Point(95+200*a, 200+100*i))
        wline2.setWidth(3)
        wline2.draw(window)
    roof = gr.Polygon(gr.Point(20+200*a, 150), gr.Point(70+200*a, 100), gr.Point(120+200*a, 150))
    roof.setFill('brown')
    roof.draw(window)


window = gr.GraphWin("Jenkslex and Ganzz project", w, h)

sky = gr.Rectangle(gr.Point(0, 0), gr.Point(w, h/2))
sky.setFill('blue')

ground = gr.Rectangle(gr.Point(0, h/2), gr.Point(w, h))
ground.setFill('green')

sky.draw(window)
ground.draw(window)

sun = gr.Circle(gr.Point(700, 50), 60)#радиус солнца увеличил
sun.setFill('yellow')
sun.draw(window)

cloudx1 = 100
cloudy1 = 20
cloud_distance = 30
n = 8

for i in range(1, n):
    a=cloudy1 + random.randint(1, 600)/ 100 * cloud_distance
    cloud(cloudx1 * i, a, 30)
    cloud(cloudx1 * i, a+50, 30)

for i in range(4):#клонирвал дома
    House(i)
for i in range(6):
    x=random.randint(-600, 0)
    
    tree = gr.Rectangle(gr.Point(700+x, 400), gr.Point(720+x, 430))
    tree.setFill('brown')
    tree.draw(window)

    leaflayer1 = gr.Polygon(gr.Point(670+x, 400), gr.Point(710+x, 320), gr.Point(750+x, 400))
    leaflayer1.setFill('darkgreen')
    leaflayer1.draw(window)

    leaflayer2 = gr.Polygon(gr.Point(680+x, 370), gr.Point(710+x, 290), gr.Point(740+x, 370))
    leaflayer2.setFill('darkgreen')
    leaflayer2.draw(window)

    leaflayer3 = gr.Polygon(gr.Point(685+x, 340), gr.Point(710+x, 250), gr.Point(735+x, 340))
    leaflayer3.setFill('darkgreen')
    leaflayer3.draw(window)
    
for i in range(-1, 2, 1):#клонировал тракторы
    corp = gr.Polygon(gr.Point(290+200*i, 490), gr.Point(290+200*i, 405), gr.Point(340+200*i, 405), gr.Point(350+200*i, 445), gr.Point(405+200*i, 445), gr.Point(405+200*i, 490), gr.Point(300+200*i, 490))
    corp.setFill('red')
    corp.draw(window)
    
    wind = gr.Polygon(gr.Point(295+200*i, 445), gr.Point(295+200*i, 410), gr.Point(335+200*i, 410), gr.Point(343.75+200*i, 445), gr.Point(295+200*i, 445))
    wind.setFill('black')#тонировал стекло
    wind.draw(window)

    line1 = gr.Line(gr.Point(295+200*i, 445), gr.Point(295+200*i, 490))
    line1.setFill('black')
    line1.draw(window)

    line2 = gr.Line(gr.Point(343.75+200*i, 445), gr.Point(343.75+200*i, 490))
    line2.setFill('black')
    line2.draw(window)

    handle = gr.Rectangle(gr.Point(330+200*i, 450), gr.Point(340+200*i, 453))
    handle.setFill('black')
    handle.draw(window)

    wheel(300+200*i, 485, 25, 35)#изменил размеры колес
    wheel(400+200*i, 500, 10, 20)
    
window.getMouse()

window.close()