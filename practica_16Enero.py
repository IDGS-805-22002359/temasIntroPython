import os
import math

os.system('clear')
print('Calculadora de la distancia entre dos puntos')

x1 = int(input('Ingrese el punto x1\n'))
os.system('clear')

y1 = int(input('Ingrese el punto y1\n'))
os.system('clear')

x2 = int(input('Ingrese el punto x2\n')) 
os.system('clear')

y2 = int(input('Ingrese el punto y2\n'))
os.system('clear')

res = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('La distancia entre el punto ({}, {}) y el punto ({}, {}) es {}'.format(x1, y1, x2, y2, res))
