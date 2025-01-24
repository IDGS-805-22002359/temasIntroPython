from modelo import Modelo
import os

class Repositorio:
    def __init__(self, archivo_compras='compras.txt'):
        self.archivo_compras = archivo_compras

    def guardar_compras(self, compras):
        file = open(self.archivo_compras, 'w')
        for compra in compras:
            file.write(f'{compra.nombre},{compra.compradores},{compra.boletos},{compra.total}\n')
        file.close()

    def cargar_compras(self):
        compras = []
        if os.path.exists(self.archivo_compras):
            file = open(self.archivo_compras, 'r')
            lines = file.readlines()
            for line in lines:
                nombre, compradores, boletos, total = line.strip().split(',')
                compras.append(Modelo(nombre, int(compradores), int(boletos), float(total)))
            file.close()
        return compras