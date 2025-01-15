import os

def f():
  os.system('clear')
  print('Dame dos números')
  numA = int(input('a) '))
  numB = int(input('b) '))
  print('{} + {} = {}'.format(numA, numB, numA + numB))

def g():
  os.system('clear')
  print('Dame dos números')
  numA = int(input('a) '))
  numB = int(input('b) '))
  print('{} - {} = {}'.format(numA, numB, numA - numB))

def run():
  option = int(input('1. Sumar\n2. Restar\n'))
  if option == 1:
    f()
  else:
    g()

if __name__ == '__main__':
  run()
