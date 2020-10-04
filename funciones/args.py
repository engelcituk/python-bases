def sumita(valor1, valor2, valor3, valor4):
    return valor1 + valor2 + valor3 + valor4

print(sumita(1,2,3,4))

#refactoring de la funcion anterior, cuando los argumentos son dinamicos
def sumaR(*args): #args agrupa todos los argumentos dentro de una tupla, args es una convencion, se podria llamar con otro nombre 
    total = 0
    for valor in args:
        total+= valor
    return total

print(sumaR(110, 20, 30, 40, 50))


def suma(parametro_requerido, *args): #tambien se puede poner otro argumento junto a args
  total = 0
  print(parametro_requerido)
  for valor in args:
    total+=valor
  return total

def usuarios_autenticados(**kwargs): #agrupa los argumentos en un diccionario
  print(kwargs)

usuarios_autenticados(nombre="juanito", alias="manos largas")


resultado = suma("Este es un argumento requerido",10, 20, 30, 40, 50, 60, 70)
print(resultado)

def combinacion(requerido, *args, **kwargs): #combinacion de todo lo anterior
  print(requerido)
  print(args)
  print(kwargs)

combinacion("Valor requerido", 10, 20, valor_uno=True, valor_dos=False)