diccionario = {
  'cadena': 'texto',
  'numero': 0
}

print(diccionario['cadena'])
print(type(diccionario))

diccionario['embebido'] = {
  'decimal': 1.5
}
print(diccionario)
print(diccionario['embebido'])

diccionario.pop('embebido')
print(diccionario)

diccionario['nuevo'] = {
  'lista': [1, 2, 3]
}
print(diccionario)
