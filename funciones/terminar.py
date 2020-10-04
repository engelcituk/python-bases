def miFuncion():
    print("un mensaje")
    print("segundo mensaje")
    return 2

miFuncion()
resultado = miFuncion() #al no especificar un valor a retornar el resultado será un None
print(resultado)


def mi_funcion(parametro):
  if parametro:
    return 100

resultado = mi_funcion("a")
if resultado:
  print("El resultado no es None!")