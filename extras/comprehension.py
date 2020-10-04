lista = []

for x in range(0, 101):
    lista.append(x)

#print(lista)

#nos permitiran generar estructuras de datos, ya sea una lista, tupla o diccionario
estructura = [x for x in range(0, 101) ] #list comprenhension
tupla = tuple( (x for x in range(0, 101)) ) #tuple comprenhension
tuplaPares = tuple( (x for x in range(0, 101) if x %2 == 0) ) #tuple comprenhension

diccionario = { indice:valor for indice, valor in enumerate(estructura) }
#print(tuplaPares)
print(diccionario)

