# -*- coding: utf-8 -*-
from Tkinter import *
from sys import argv
import random
import Generadores_metrosim as genMS
import generador
import Metro
import Estacion

semilla = 4564654
intervalosLlegadas = genMS.generarLlegadas(generador.mcm(semilla, 1000))
bajadas = genMS.generarBajadas(generador.mcl(semilla, 1000))
estaciones = []
metros = []
master = Tk()
canvas = Canvas(master, width=1280, height=680)
frecuencia = 5
ruleta = [0] * 40 + [1] * 10 + [2] * 10 + [3] * 40

def simulacion():
    for E in estaciones:
        if E.hayMetro:
            metros[E.metro].bajanPasajeros(canvas, master, bajadas, estaciones)
            E.subenPasajeros(canvas, master, metros)
            metros[E.metro].mover(canvas, 170, 0, estaciones)
            E.hayMetro = False
        else:
            E.lleganPasajeros(canvas, master, frecuencia, intervalosLlegadas, ruleta)


    for M in metros:
        M.frecuencia -= frecuencia
        if M.frecuencia <= 0:
            if M.posicion >= 8:
                M.mover(canvas, -(170*8), 0, estaciones)
                M.posicion = 0
                M.frecuencia = frecuencia
            else:
                M.mover(canvas, 170, 0, estaciones)
                M.frecuencia = frecuencia



    master.after(500, simulacion)


canvas.pack()
b=Button(master, text=u'\u25B6', padx=10, fg='green', font=('TkDefaultFont', 32))
b.pack(side='left')
canvas.create_line(0, 680/2, 1280, 680/2, dash=(30), width=3.0)

for i in xrange(0, 4):
    estaciones.append(Estacion.Estacion())
    estaciones[i].dibujar(canvas, 'Estación '+ str(i+1))
    estaciones[i].mover(canvas, 340 * i, 0)


for i in xrange(0, 4):
    metros.append(Metro.Metro(i, i, 5*(i*2 +1), 20))
    metros[i].dibujar(canvas)


master.after(1000, simulacion)


mainloop()
