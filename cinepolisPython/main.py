from controlador import Controlador
from util import print_line
import os

def main():
    controlador = Controlador()
    
    while True:
        os.system('clear')
        print('Bienvenido a la tienda de boletos')

        print_line()
        print('a) Comprar boletos')
        print('b) Salir\n')
        opcion = input('Seleccione una opción: ')
        
        if opcion == 'a':
            controlador.comprar()
        elif opcion == 'b':
            controlador.mostrar_compras()
            break
        else:
            print('Opción no válida, por favor intente de nuevo.')

if __name__ == '__main__':
    main()