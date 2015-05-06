colores = [ 'white', 'red', 'green', 'blue', 'cyan', 'yellow']
class Metro():
        def __init__(self, color, numero,frecuencia, capacidad):
                self.vagones = 4
                self.capacidad = capacidad
                self.color = colores[color]
                self.frecuencia = frecuencia
                self.pasajeros = [0, 0, 0, 0]
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
                
        def bajarPasajero(self, estacion):
                pass
        def subirPasajero(self, estacion):
                pass

        def dibujar(self, canvas):
                self.componentes.append(canvas.create_rectangle(-160, 680/2 + 10, -120, 680/2 - 10, fill=self.color))
                self.componentes.append(canvas.create_text(-140, 680/2, text='0'))
                self.componentes.append(canvas.create_rectangle(-115, 680/2 + 10, -75, 680/2 - 10, fill=self.color))
                self.componentes.append(canvas.create_text(-95, 680/2, text='0'))
                self.componentes.append(canvas.create_rectangle(-70, 680/2 + 10, -30, 680/2 - 10, fill=self.color))
                self.componentes.append(canvas.create_text(-50, 680/2, text='0'))
                self.componentes.append(canvas.create_rectangle(-25, 680/2 + 10, 15, 680/2 - 10, fill=self.color))
                self.componentes.append(canvas.create_text(-5, 680/2, text='0'))
