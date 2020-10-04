
#comprimir y descomprimir tuplas

tupla = (1,2,3,4) # se definen con parentesis, son inmutables osea que no se pueden modificar sus elementos
#uno, dos, tres, cuatro = tupla[0], tupla[1], tupla[2], tupla[3]

"""la tupla se asigna a 4 variables, reduciendo el codigo anterior, pero deben de coicidir el num. de variables con los elementos de la tupla
de lo contrario python dará un error
"""
uno, dos, tres, cuatro = tupla 

print(uno)
print(dos)
print(tres)
print(cuatro,'\n')

tuplaDos = (1,2,3,4,5, 6)
uno, dos, tres, *cuatro = tuplaDos #si hay error se pude resolver con el asterisco en la ultima variable o cualquiera de las existentes

print(uno)
print(dos)
print(tres)
print(cuatro)
#generando una nueva tupla-> tupla más una lista
tuplaTres = (1, 2, 3, 4, 5, 6 )
lista = [10, 20, 30, 40]
resultado = zip(tupla, lista)#puede recibir n cantidad de tuplas o listas
tupla = tuple(resultado)


print(tupla)


