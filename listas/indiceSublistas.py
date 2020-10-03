cursos = ['python','django','flask','c','c++','c#','java','php'] #los indices comienzan en cero

curso = cursos[0]
ultimoCurso = cursos[-1] #trae el ultimo elemento de la lista
penultimoCurso = cursos[-2] #trae el penultimo elemento de la lista

print(curso)
print(ultimoCurso)
print(penultimoCurso)

# [1:5:5] -> desde:hasta:salto
sublista = cursos[0:3] #obtener los primeros 3 elementos de la lista, se puede omitir el 0
print('sublista', sublista)
sublista2 = cursos[3:] #obtener los elementos de la lista a partir del indice 3
print('sublista2', sublista2)
sublista3 = cursos[:] #si no se indica los valores, se obtiene la lista completa
print('sublista3', sublista3)
sublistaConSaltos = cursos[1:7:2] #obtener los elementos a partir del indice uno hasta el indice 7, con saltos de dos en dos
print('sublistaConSaltos', sublistaConSaltos)
listaInversa = cursos[::-1] #muestra la lista de manera inversa
print('listaInversa', listaInversa)


