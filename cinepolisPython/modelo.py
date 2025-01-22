import json

class Modelo:

    nombre = ''
    compradores = 0
    boletos = 0
    total = 0

    def __init__(self, nombre, compradores, boletos, total):
        self.nombre = nombre
        self.compradores = compradores
        self.boletos = boletos
        self.total = total

    def __str__(self):
        return json.dumps({
            'nombre': self.nombre,
            'compradores': self.compradores,
            'boletos': self.boletos,
            'total': self.total
        })