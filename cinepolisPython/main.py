from controlador import Controlador
from util import print_line
from datetime import datetime
import os

def main():
    controlador = Controlador()
    
    while True:
        os.system('clear')
        print('¡Bienvenido(a) a UTPólis!			{}'.format(datetime.today().strftime('%d/%m/%Y %H:%M:%S')))

        print_line()
        print('a) Comprar boletos')
        print('b) Mostrar compras')
        print('c) Salir\n')
        opcion = input('Seleccione una opción: ').lower()
        
        if opcion == 'a' or opcion == 'comprar':
            controlador.comprar()
        elif opcion == 'b' or opcion == 'mostrar':
            controlador.mostrar_compras()
        elif opcion == 'c' or opcion == 'salir':
            os.system('clear')
            break
        else:
            print('Opción no válida, por favor intente de nuevo.')

if __name__ == '__main__':
    main()
