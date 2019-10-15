from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

balls = []

colors = ['red','orange','yellow','green','blue']
def new_ball():
    global number_ball, balls
    ball = {'id': 0, 'x': rnd(100,700), 'y': rnd(100,500), 'r': rnd(30,50), 'vx': rnd(-5,5), 'vy': rnd(-5,5), 'col': choice(colors), 'del': 0}
    ball['id'] = canv.create_oval(ball['x'] - ball['r'], ball['y'] - ball['r'], ball['x'] + ball['r'], ball['y'] +ball['r'],fill = ball['col'], width=0)
    balls.append(ball)
    root.after(rnd(300,1000),new_ball)


def change_coordinates():
    global balls
    for b in balls:
        if b['del'] == 0:
            if b['x'] + b['r'] >= 800:
                b['vx'] = -b['vx']
            if b['x'] - b['r'] <= 0:
                b['vx'] = -b['vx']
            if b['y'] + b['r'] >= 600:
                b['vy'] = -b['vy']
            if b['y'] - b['r'] <= 0:
                b['vy'] = -b['vy']
            b['x'] = b['x'] + b['vx']
            b['y'] = b['y'] + b['vy']
            canv.delete(b['id'])
            b['id'] = canv.create_oval(b['x'] - b['r'], b['y'] - b['r'], b['x'] + b['r'], b['y'] +b['r'],fill = b['col'], width=0)
    root.after(50,change_coordinates) 

score = Label(root, bg='black', fg='white', width=20)
score.pack
bal = 0

def click(event):
    global bal, balls
    x1 = event.x
    y1 = event.y   
    for b in balls:
        if (b['x'] - x1)**2 + (b['y'] - y1)**2 <= b['r']**2:
            bal += 1
            score['text'] = bal
            score.pack()
            b['del'] = 1
            canv.delete(b['id'])


b = Entry(canv, width=20)
b.bind('<Button-1>', click)

new_ball()
change_coordinates()
canv.bind('<Button-1>', click)
mainloop()