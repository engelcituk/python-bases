
diccionario = {"a":1, "b":2, "c":3, "a":4} 
resultado = diccionario["a"] #si no se encuentra el valor para esa llave, python da un error
resultado2 = "z" in diccionario #para saber si existe en el diccionario, regresa un booleano
resultado3 = diccionario.get("z","la llave no existe") #sino se encuentra el valor python regresa un None o muestra el mensaje del segundo argumento
resultado4 = diccionario.setdefault("z",{}) #sino se encuentra el valor para esa llave python le asigna un valor a esa llave


print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)

