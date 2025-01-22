
class Operacion:
  
  # Atributos
  numA = 0
  numB = 0
  res = 0  

  # Método constructor
  def __init__(self, numA, numB):
    self.numA = numA
    self.numB = numB


  # Todos los métodos
  def sumar(self):
    self.res = self.numA + self.numB
    print('La suma es {}'.format(self.res))

def main():
  operacion = Operacion(3, 4)
  operacion.sumar()

if __name__ == '__main__':
  main()
