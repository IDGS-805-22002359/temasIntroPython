from io import open
import os

text = 'Una línea con texto.\n' + 'Otra línea con texto.\n'

file = open('file.txt', 'w')
file.write(text)

cadena = 'Otra cadena.\n'
file.write(cadena)
file.close()

salida = 'Test.\n'
file.write(salida)
