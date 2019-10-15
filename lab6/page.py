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
    ball = {'id': 0, 'x': rnd(100,700), 'y': rnd(100,500), 'r': rnd(30,50)}
    ball['id'] = canv.create_oval(ball['x'] - ball['r'], ball['y'] - ball['r'], ball['x'] + ball['r'], ball['y'] +ball['r'],fill = choice(colors), width=0)
    balls.append(ball)
    root.after(rnd(300,1000),new_ball)

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
            canv.delete(b['id'])


b = Entry(canv, width=20)
b.bind('<Button-1>', click)

new_ball()
canv.bind('<Button-1>', click)
mainloop()