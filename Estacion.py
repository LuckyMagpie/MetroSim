class Estacion():
        def __init__(self):
                self.pasajeros = [0, 0, 0, 0]
                self.subieron = 0
                self.bajaron= 0
                self.componentes = []

        def llegaPasajeros(self):
                pass
                
        def dibujar(self, canvas, nombre):
                self.componentes.append(canvas.create_text(95, 680/2 + 20, text=nombre))
                self.componentes.append(canvas.create_rectangle(10, 680/2 + 30, 185, 680/2 + 80, fill='white'))
                self.componentes.append(canvas.create_text(30, 680/2 + 55, text='0'))
                self.componentes.append(canvas.create_text(75, 680/2 + 55, text='0'))
                self.componentes.append(canvas.create_text(120, 680/2 + 55, text='0'))
                self.componentes.append(canvas.create_text(165, 680/2 + 55, text='0'))

        def mover(self, canvas, cantidadX, cantidadY):
                for comp in self.componentes:
                        canvas.move(comp, cantidadX, cantidadY)

