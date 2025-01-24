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
        
        if not self.solicitar_nombre():
            return None
        
        while True:
            if not self.solicitar_compradores():
                return None
            
            if not self.solicitar_boletos():
                return None
            
            if self.validar():
                break

        self.calcular_descuento()
        self.confirmar_compra()

    def solicitar_nombre(self):
        while True:
            os.system('clear')
            print('Ingrese el nombre del comprador:\n\n')
            nombre = input()
            if nombre == '':
                return False
            self.nombre = nombre
            return True

    def solicitar_compradores(self):
        while True:
            os.system('clear')
            print('Comprador : ', self.nombre)
            print_line()
            print('Ingrese el total de compradores:\n\n')
            entrada = input()
            if entrada == '':
                if not self.solicitar_nombre():
                    return False
                continue
            self.compradores = int(entrada)
            if self.compradores == 0:
                return False
            return True

    def solicitar_boletos(self):
        while True:
            os.system('clear')
            print('Comprador : ', self.nombre)
            print('Cantidad de compradores : ', self.compradores)
            print_line()
            print('Ingrese el total de boletos:\n\n')
            entrada = input()
            if entrada == '':
                if not self.solicitar_compradores():
                    return False
                continue
            self.boletos = int(entrada)
            if self.boletos == 0:
                return False
            return True

    def calcular_descuento(self):
        if self.boletos > 5:
            self.descuento = 0.15
        elif self.boletos <= 5 and self.boletos >= 3:
            self.descuento = 0.10

    def confirmar_compra(self):
        while True:
            os.system('clear')
            print('Comprador : ', self.nombre)
            print('Cantidad de compradores : ', self.compradores)
            print('Cantidad de boletos : ', self.boletos)
            print_line()
            opcion = input('¿Tarjeta CINECO? (s/n): ').lower()
            if opcion == '':
                if not self.solicitar_boletos():
                    return None
                continue
            total = (self.boletos * self.precioBoleto) - (self.boletos * self.precioBoleto * self.descuento)
            if opcion == 's' or opcion == 'si':
                total = total - (total * 0.10)
            break

        while True:
            os.system('clear')
            print('Comprador : ', self.nombre)
            print('Cantidad de compradores : ', self.compradores)
            print('Cantidad de boletos : ', self.boletos)
            print('Total a pagar : $ ', total)
            print_line()
            opcion = input('¿Confirmar compra? (s/n): ').lower()
            if opcion == '':
                continue
            if opcion == 'n' or opcion == 'no':
                if not self.solicitar_tarjeta_cineco():
                    return None
                continue
            break

        nuevo = Modelo(self.nombre, self.compradores, self.boletos, total)
        self.compras.append(nuevo)
        self.repositorio.guardar_compras(self.compras)

        os.system('clear')
        print_line()
        print(f'Comprador: {self.nombre}')
        print(f'Cantidad de compradores: {self.compradores}')
        print(f'Cantidad de boletos: {self.boletos}')
        print(f'Total a pagar: $ {total}')
        print_line()
        print('Presiona ENTER para volver al menú principal.')
        input()

        return nuevo

    def solicitar_tarjeta_cineco(self):
        while True:
            os.system('clear')
            print('Comprador : ', self.nombre)
            print('Cantidad de compradores : ', self.compradores)
            print('Cantidad de boletos : ', self.boletos)
            print_line()
            opcion = input('¿Tarjeta CINECO? (s/n): ').lower()
            if opcion == '':
                if not self.solicitar_boletos():
                    return False
                continue
            if opcion == 's' or opcion == 'si':
                self.total = (self.boletos * self.precioBoleto) - (self.boletos * self.precioBoleto * (self.descuento + 0.10))
            else:
                self.total = (self.boletos * self.precioBoleto) - (self.boletos * self.precioBoleto * self.descuento)
            return True
    
    def validar(self):
        while self.boletos > self.maxBoletos * self.compradores:
            os.system('clear')
            print('No hay suficientes boletos, por favor modifique la cantidad de boletos o la cantidad de compradores')
            print_line()
            print('1. Modificar cantidad de boletos')
            print('2. Modificar cantidad de compradores\n\n')
            opcion = int(input('Seleccione una opción: '))
            if opcion == 0:
                return False
            os.system('clear')
            if opcion == 1:
                print('Ingrese el total de boletos:\n\n')
                self.boletos = int(input())
                if self.boletos == 0:
                    return False
            elif opcion == 2:
                print('Ingrese el total de compradores:\n\n')
                self.compradores = int(input())
                if self.compradores == 0:
                    return False
        return True
    
    def mostrar_compras(self):
        while True:
            total_general = 0
            os.system('clear')
            i = 1
            for compra in self.compras:
                print(str(i) + '. ' + str(compra))
                total_general += compra.total
                i += 1
            print(f'\n\n$ {total_general} total general 💸')
            print_line()
            print('Presiona ENTER para volver al menú principal.') 
            input()
            break   
        return None