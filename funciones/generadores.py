#tipo especial de funcion que podemmos utilizar para la creacion de una secuencia de datos
def tabla_multiplicar(numero, maximo=10):
  for posicion in range(1, maximo+1):
    yield numero * posicion, numero, posicion #retorna la funcion sin terminar la funcion tabla_multiplicar y tambien retornar mas valores


for resultado, numero, posicion in tabla_multiplicar(9, 5):
  print(numero, "*", posicion, "=", resultado)