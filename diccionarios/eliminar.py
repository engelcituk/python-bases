diccionario  = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8}

del diccionario["a"] #para borrar un elemento del diccionario, en base a su llave
valor = diccionario.pop("b") #para borrar un elemento del diccionario, en base a su llave, pop retorna el valor que se ha eliminado de la llave

#diccionario = {} #para eliminar todos los elementos de un diccionario
diccionario.clear() #para borrar todos los elementos del diccionario

print(len(diccionario))
print(diccionario)
print(valor)

