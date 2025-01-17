lista1 = [10, 5, 3]
lista2 = [1.5, 2.66, 1.70, 89.2]
lista3 = ['Lunes', 'Martes', 'Miércoles']
lista4 = ['Juan', 45, 1.92]

print(type(lista1))
print(len(lista1))
print(lista1[0])

i = 0
suma = 0
while i < len(lista1):
  suma += lista1[i]
  i += 1

print('La suma es ', suma)
print(lista1)
print(lista1[0])
lista1.append(100)
print(lista1)
print(lista1[3])

lista5 = []
for i in range(5):
  valor = int(input('Por favor dame un número\n'))
  lista5.append(valor)

print(lista5)

print(lista1)
lista1.pop()
print(lista1)

lista1.sort()
print(lista1)

lista1.reverse()
print(lista1)

lista1.remove(10)
print(lista1)

lista1.clear()
print(lista1)

'''
Crear un programa, pedir una cantidad n de números y almacenarlos en un arreglo
la salida deberá ser la siguiente:

Lista completa: xxxxxx
Pares: aaaa
Impares: bbbb
'''

lista = []
pares = []  
impares = []

for i in range(5):
  valor = int(input('Ingresa el número {}: \n'.format(i + 1)))
  lista.append(valor)

lista.sort()

for valor in lista:
  if(valor % 2 == 0):  
    pares.append(valor)
  else:
    impares.append(valor)

print(lista)
print(pares)
print(impares)

