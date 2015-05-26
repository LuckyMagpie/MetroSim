import random
import time
class Estacion():
    def __init__(self):
        self.pasajeros = [0, 0, 0, 0]
        self.subieron = 0
        self.bajaron= 0
        self.hayMetro = False
        self.metro = 0
        self.componentes = []
        self.enEspera = [0, 0, 0, 0]

    def lleganPasajeros(self, canvas, master ,frecuencia, intervalosLlegadas, ruleta, pico):
        tiempo = frecuencia * 60
        while tiempo > 0:
            intervalo = random.choice(intervalosLlegadas)
            if intervalo < tiempo:
                pos = random.choice(ruleta)
                tiempo -= intervalo
                if pico == 'S' and random.choice([True, False]):
                    self.pasajeros[pos] += 1
                self.pasajeros[pos] += 1
                canvas.itemconfig(self.componentes[pos+2], text=str(self.pasajeros[pos]))
                canvas.update()
                master.after(50)
            else:
                tiempo = 0

    def dibujar(self, canvas, nombre):
        self.componentes.append(canvas.create_text(95, 680/2 + 20, text=nombre))
        self.componentes.append(canvas.create_rectangle(10, 680/2 + 30, 185, 680/2 + 80, fill='white'))
        self.componentes.append(canvas.create_text(30, 680/2 + 55, text='0'))
        self.componentes.append(canvas.create_text(75, 680/2 + 55, text='0'))
        self.componentes.append(canvas.create_text(120, 680/2 + 55, text='0'))
        self.componentes.append(canvas.create_text(165, 680/2 + 55, text='0'))
        self.componentes.append(canvas.create_text(220, 680/2 + 80, text='Bajadas: 0', fill='red'))
        self.componentes.append(canvas.create_text(220, 680/2 + 30, text='Subidas: 0', fill='blue'))
        self.componentes.append(canvas.create_text(30, 680/2 + 95, text='0', fill='red'))
        self.componentes.append(canvas.create_text(75, 680/2 + 95, text='0', fill='red'))
        self.componentes.append(canvas.create_text(120, 680/2 + 95, text='0', fill='red'))
        self.componentes.append(canvas.create_text(165, 680/2 + 95, text='0', fill='red'))
        self.componentes.append(canvas.create_text(100, 680/2 + 115, text='No pudieron abordar', fill='red'))

    def mover(self, canvas, cantidadX, cantidadY):
        for comp in self.componentes:
                canvas.move(comp, cantidadX, cantidadY)

    def subenPasajeros(self, canvas, master, metros):
        canvas.itemconfig(self.componentes[7], text='Subidas: 0')
        if sum(self.pasajeros) > 0:
            texto = 0
            for i in xrange(0, 4):
                while metros[self.metro].checarCap(i) and (self.pasajeros[i] > 0):
                    texto += 1
                    self.pasajeros[i] -= 1
                    metros[self.metro].pasajeros[i] += 1
                    canvas.itemconfig(self.componentes[i + 2], text=str(self.pasajeros[i]))
                    canvas.itemconfig(metros[self.metro].componentes[i + 4], text=str(metros[self.metro].pasajeros[i]))
                    canvas.itemconfig(self.componentes[7], text='Subidas: ' + str(texto))
                    canvas.update()
                    canvas.after(50)

            for i in xrange(0, 4):
                self.enEspera[i] += self.pasajeros[i]
                canvas.itemconfig(self.componentes[i + 8], text=str(self.enEspera[i]))

            metros[self.metro].calcularCap(canvas)
            canvas.update()
