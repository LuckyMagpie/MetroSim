# -*- coding: utf-8 -*-
from Tkinter import *
from sys import argv
from multiprocessing import Pool
import Metro
import Estacion

estaciones = []
metros = []
master = Tk()
canvas = Canvas(master, width=1280, height=680)
frecuencia = 5
 
    
def simulacion():
    for E in estaciones:
        if E.hayMetro:
            #Bajar pasajeros
            #subir pasajeros
            #mover metro
            pass
        else:
            #generar pasajeros en esa estacion
            pass
    
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
                
    print estaciones[1].metro    
    master.after(1000, simulacion)


canvas.pack()
canvas.create_line(0, 680/2, 1280, 680/2, dash=(30), width=3.0)

for i in xrange(0, 4):
    estaciones.append(Estacion.Estacion())
    estaciones[i].dibujar(canvas, 'Estación '+ str(i+1))
    estaciones[i].mover(canvas, 340 * i, 0)


for i in xrange(0, 6):
    metros.append(Metro.Metro(i, i, 5, 200))
    metros[i].dibujar(canvas)


master.after(1000, simulacion)


mainloop()
