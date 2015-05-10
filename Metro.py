import random
colores = [ 'white', 'red', 'green', 'cyan']
class Metro():
        def __init__(self, color, numero,frecuencia, capacidad):
                self.vagones = 4
                self.capacidad = capacidad
                self.color = colores[color]
                self.frecuencia = frecuencia
                self.pasajeros = [5, 4, 3, 2]
                self.componentes = []
                self.numero = numero
                self.posicion = 0
               
        def mover(self, canvas, cantidadX, cantidadY, estaciones):
                for comp in self.componentes:
                        canvas.move(comp, cantidadX, cantidadY)
                if self.posicion < 8:
                        self.posicion += 1
                
                if self.posicion % 2 != 0:
                        estaciones[int(self.posicion/2)].hayMetro = True
                        estaciones[int(self.posicion/2)].metro = self.numero
                
      
        def dibujar(self, canvas):
                self.componentes.append(canvas.create_rectangle(-160, 680/2 + 10, -120, 680/2 - 10, fill=self.color))
                self.componentes.append(canvas.create_rectangle(-115, 680/2 + 10, -75, 680/2 - 10, fill=self.color))
                self.componentes.append(canvas.create_rectangle(-70, 680/2 + 10, -30, 680/2 - 10, fill=self.color))
                self.componentes.append(canvas.create_rectangle(-25, 680/2 + 10, 15, 680/2 - 10, fill=self.color))
                self.componentes.append(canvas.create_text(-140, 680/2, text=str(self.pasajeros[0])))
                self.componentes.append(canvas.create_text(-95, 680/2, text=str(self.pasajeros[1])))
                self.componentes.append(canvas.create_text(-50, 680/2, text=str(self.pasajeros[2])))
                self.componentes.append(canvas.create_text(-5, 680/2, text=str(self.pasajeros[3])))
                self.componentes.append(canvas.create_text(-80, 680/2 - 20, text='Capacidad = ' + str((sum(self.pasajeros) / float((self.capacidad * 4))) * 100) + '%'))


        def bajanPasajeros(self, canvas, master, bajadas, estaciones):
                canvas.itemconfig(estaciones[int(self.posicion/2)].componentes[6], text='Bajadas: 0')
                if sum(self.pasajeros) > 0:
                        pasajeros = random.choice(bajadas)
                        texto = 0
                        posibilidades = [0, 1, 2, 3]
                        while pasajeros > 0:
                                if posibilidades:
                                        vagon = random.choice(posibilidades)
                                        if self.pasajeros[vagon] > 0:
                                                self.pasajeros[vagon] -= 1
                                                pasajeros -= 1
                                                texto += 1
                                                canvas.itemconfig(self.componentes[vagon + 4], text=str(self.pasajeros[vagon]))
                                                canvas.itemconfig(estaciones[int(self.posicion/2)].componentes[6], text='Bajadas ' + str(texto))
                                                canvas.update()
                                                master.after(150)
                                        else:
                                                posibilidades.remove(vagon)
                                else:
                                        pasajeros = 0
                        canvas.itemconfig(self.componentes[8], text='Capacidad = ' + str((sum(self.pasajeros) / float((self.capacidad * 4))) * 100) + '%')
                        canvas.update()
