# -*- coding: utf-8 -*-
from Tkinter import *
from sys import argv
import random
import Generadores_metrosim as genMS
import Generador
import Metro
import Estacion

try:
    semilla = int(argv[1])
except:
    semilla = int(input("Semilla: "))

try:
    frecuencia = int(argv[2])
except:
    frecuencia = int(input("Frecuencia de llegada del metro (minutos): "))

intervalosLlegadas = genMS.generarLlegadas(Generador.mcm(semilla, 2000))
bajadas = genMS.generarBajadas(Generador.mcl(semilla, 2000))
estaciones = []
metros = []
master = Tk()
canvas = Canvas(master, width=1280, height=680)
ruleta = [0] * 30 + [1] * 20 + [2] * 20 + [3] * 30

def stop():
    raw_input("Presiona Enter para continuar")

def simulacion(tiempo):
    for E in estaciones:
        if E.hayMetro:
            metros[E.metro].bajanPasajeros(canvas, master, bajadas, estaciones)
            E.subenPasajeros(canvas, master, metros)
            E.hayMetro = False
            metros[E.metro].mover(canvas, 170, 0, estaciones)
        E.lleganPasajeros(canvas, master, frecuencia, intervalosLlegadas, ruleta)

    tiempo += frecuencia
    canvas.itemconfig(tiempoTxt, text='Tiempo: '+ str(tiempo)+ ' minutos')
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

    master.after(500, simulacion, tiempo)

canvas.pack()
tiempo = 0
tiempoTxt = canvas.create_text(1280/2, 10, text='Tiempo: 0 minutos', font=('TkDefaultFont', 16))
stopB = Button(master, text=u'\u25A0', padx=10, fg='red', font=('TkDefaultFont', 32), command=stop)
stopB.pack(side='left')
canvas.create_line(0, 680/2, 1280, 680/2, dash=(30), width=3.0)

for i in xrange(0, 4):
    estaciones.append(Estacion.Estacion())
    estaciones[i].dibujar(canvas, 'Estación '+ str(i+1))
    estaciones[i].mover(canvas, 340 * i, 0)

for i in xrange(0, 4):
    metros.append(Metro.Metro(i, i, frecuencia*(i*2 + 1), 150))
    metros[i].dibujar(canvas)

master.after(1000, simulacion, tiempo)

mainloop()
