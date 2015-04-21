colores = [ 'white', 'red', 'green', 'blue', 'cyan', 'yellow']
class Metro():
        def __init__(self, c, frecuencia, capacidad):
                self.vagones = 4
                self.capacidad = capacidad
                self.color = colores[c]
                self.frecuencia = frecuencia
                self.pasajeros = [0, 0, 0, 0]
               
        def mover(self):
                pass
        def bajarPasajero(self, estacion):
                pass
        def subirPasajero(self, estacion):
                pass

        def dibujar(self, canvas):
                canvas.create_rectangle(10, 680/2 + 10, 50, 680/2 - 10, fill=self.color)
                canvas.create_text(30, 680/2, text='0')
                canvas.create_rectangle(55, 680/2 + 10, 95, 680/2 - 10, fill=self.color)
                canvas.create_text(75, 680/2, text='0')
                canvas.create_rectangle(100, 680/2 + 10, 140, 680/2 - 10, fill=self.color)
                canvas.create_text(120, 680/2, text='0')
                canvas.create_rectangle(145, 680/2 + 10, 185, 680/2 - 10, fill=self.color)
                
                canvas.create_text(165, 680/2, text='0')        
