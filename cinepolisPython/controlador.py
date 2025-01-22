from servicio import Servicio

class Controlador:

    def __init__(self):
        self.servicio = Servicio()
        
    def comprar(self):
        self.servicio.comprar()
        
    def mostrar_compras(self):
        self.servicio.mostrar_compras()