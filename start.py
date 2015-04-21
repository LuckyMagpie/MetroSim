# -*- coding: utf-8 -*-
from Tkinter import *
from sys import argv
import Metro
import Estacion

master = Tk()

canvas = Canvas(master, width=1280, height=680)
canvas.pack()
canvas.create_line(0, 680/2, 1280, 680/2, dash=(30), width=3.0)
Metro.Metro(1,1,1).dibujar(canvas)
m = Estacion.Estacion()
m.dibujar(canvas, 'Estacion 1')






mainloop()
