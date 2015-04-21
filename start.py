# -*- coding: utf-8 -*-
from Tkinter import *
from sys import argv
import Metro
import Estacion

estaciones = []
metros = []
master = Tk()

def test(m, canvas):
    m.mover(canvas, 40, 0)
    master.after(1000, test,m,canvas)

canvas = Canvas(master, width=1280, height=680)
canvas.pack()
canvas.create_line(0, 680/2, 1280, 680/2, dash=(30), width=3.0)

for i in xrange(0, 4):
    estaciones.append(Estacion.Estacion())
    estaciones[i].dibujar(canvas, 'Estación '+ str(i+1))
    estaciones[i].mover(canvas, 340 * i, 0)



m = Metro.Metro(1,1,1)
m.dibujar(canvas)
master.after(1000, test, m, canvas)


mainloop()
