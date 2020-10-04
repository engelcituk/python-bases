#un decorador es poara modificar una funcion existente sin cambiar sus lineas de codigo, comunmente para agregar mayor funcionalidad

#a, b, c
#a(b) -> c donde a recibe como parametro a b para dar como salida a c

def decorador(funcion):
  
  def nueva_funcion(*args, **kwargs): #funcion c
    print("Podemos agregar código antes")
    resultado = funcion(*args, **kwargs)
    print("Podemos agregar código después")
    return resultado

  return nueva_funcion


@decorador
def funcion_a_decorar(): #funcion b
  print("Este es una función a decorar")

@decorador 
def suma(val1, val2):
  return val1 + val2


funcion_a_decorar()

print("\n")

resultado = suma(10, 20)
print(resultado)