lista = [8.17, 90, 1, 5, 44, 1.32]
#ordena la lista de forma ascendente
lista.sort() 
menor = lista[0]
print(lista, 'el menor es', menor)
 #ordena la lista de forma descendente
lista.sort(reverse=True)
mayor = lista[0]
print(lista, 'el mayor es', mayor)
#otra opcion es usar min y max
menor2 = min(lista)
print(lista, 'el menor con funcion min es:', menor2)
mayor = max(lista)
print(lista, 'el mayor con funcion max es:', mayor)
#para saber la longitud de la lista
longitud = len(lista)
print('La longitud de la lista es:', longitud)
#verificar si el elemento 8 existe en la lista
resultado = 8 in lista
print('El valor 8 existe en la lista:', resultado)
#si elemento existe en la lista, obtener en que indice está
indice = lista.index(90)
print('90 está en el indice:', indice) #da 0 debido a que está ordenado
#para saber cuantas veces existe un elemento en la lista
contador =  lista.count(5)
print('Las veces que 5 se repite en la lista:', contador)#si no se encuentra, el resultado será cero


