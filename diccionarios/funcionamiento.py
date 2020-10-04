diccionario = {}

diccionario["nombre"] = "Code" #para agregar una llave con su valor
valor = diccionario["nombre"] #obtener el valor de la llave
diccionario["nombre"] = 40 #se le agrega el nuevo valor

print(diccionario)
print(valor)

diccionario2 = {"a":1, "b":2, "c":3, "a":4} #no pueden existir llaves duplicadas, si se repiten se toma la ultima llave ingresada
print(diccionario2)
