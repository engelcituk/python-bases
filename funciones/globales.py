animal = 'León' #Es una variable global

def mostrar_animal():
  global animal #con esto modificamos el valor de la variable global desde una funcion
  animal = 'Ballena' #variables locales
  print(animal)

mostrar_animal()
print(animal)