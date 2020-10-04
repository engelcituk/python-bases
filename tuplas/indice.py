tupla = (1,2,3,4,5,6,7,8,9,0) # se definen con parentesis, son inmutables osea que no se pueden modificar sus elementos

elemento = tupla[4]
ultimoElemento= tupla[-1] #trae el ultimo elemento de la lista
penultimoElemento= tupla[-2] #trae el penultimo elemento de la lista
subTupla = tupla[0:4]#posicion inicial:final
subTuplaConSaltos = tupla[1:7:2] #obtener los elementos a partir desde:hasta:saltos 


print(tupla)
print(elemento)
print('ultimoElemento',ultimoElemento)
print('penultimoElemento',penultimoElemento)
print('subTupla',subTupla)
print('subTuplaConSaltos',subTuplaConSaltos)


