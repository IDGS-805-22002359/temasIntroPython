from modelo import Modelo
from repositorio import Repositorio
from util import print_line
import os

class Servicio:
    
    boletos = 0
    compradores = 0
    maxBoletos = 7
    precioBoleto = 12
    descuento = 0
    
    def __init__(self):
        self.repositorio = Repositorio()
        self.compras = self.repositorio.cargar_compras()
    
    def comprar(self):
        os.system('clear')
        
        print('El precio de hoy para los boletos es de $ {} por boleto'.format(self.precioBoleto))
        print_line()
        print('Ingrese el nombre del comprador:\n\n')
        self.nombre = input()
        
        while True:
            os.system('clear')
            print('Comprador : ', self.nombre)
            print_line()
            print('Ingrese el total de compradores:\n\n')
            self.compradores = int(input())
            
            os.system('clear')
            print('Comprador : ', self.nombre)
            print('Cantidad de compradores : ', self.compradores)
            print_line()
            print('Ingrese el total de boletos:\n\n')
            self.boletos = int(input())
            
            if self.validar():
                break

        if self.boletos > 5:
            self.descuento = 0.15
        elif self.boletos <= 5 and self.boletos >= 3:
            self.descuento = 0.10

        os.system('clear')
        print('Comprador : ', self.nombre)
        print('Cantidad de compradores : ', self.compradores)
        print('Cantidad de boletos : ', self.boletos)
        print_line()
        opcion = input('¿Tarjeta CINECO? (s/n): ')

        if opcion == 's':
            total = (self.boletos * self.precioBoleto) - (self.boletos * self.precioBoleto * (self.descuento + 0.10))
        else:
            total = (self.boletos * self.precioBoleto) - (self.boletos * self.precioBoleto * self.descuento)

        os.system('clear')
        print('Comprador : ', self.nombre)
        print('Cantidad de compradores : ', self.compradores)
        print('Cantidad de boletos : ', self.boletos)
        print('Total a pagar : $ ', total)
        print_line()
        opcion = input('¿Confirmar compra? (s/n): ')

        if opcion == 'n':
            return None

        nuevo = Modelo(self.nombre, self.compradores, self.boletos, total)
        self.compras.append(nuevo)
        self.repositorio.guardar_compras(self.compras)
        return nuevo
    
    def validar(self):
        while self.boletos > self.maxBoletos * self.compradores:
            os.system('clear')
            print('No hay suficientes boletos, por favor modifique la cantidad de boletos o la cantidad de compradores')
            print_line()
            print('1. Modificar cantidad de boletos')
            print('2. Modificar cantidad de compradores\n\n')
            opcion = int(input('Seleccione una opción: '))
            os.system('clear')
            if opcion == 1:
                print('Ingrese el total de boletos:\n\n')
                self.boletos = int(input())
            elif opcion == 2:
                print('Ingrese el total de compradores:\n\n')
                self.compradores = int(input())
        return True
    
    def mostrar_compras(self):
        total_general = 0
        os.system('clear')
        i = 1
        for compra in self.compras:
            print(str(i) + '. ' + str(compra))
            total_general += compra.total
            i += 1
        print(f'\n\n$ {total_general} total general\n\n')