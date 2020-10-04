texto = "Este es una cadena" # los strings al igual que las tuplas, son inmutables

resultado = len(texto); #para saber la longitud de la cadena
print(resultado)

primeraLetra = texto[0] #similar a hacerlo con las lista o tuplas
ultimaLetra = texto[-1] #trae el ultimo elemento del string
penultimaLetra = texto[-2] #trae el penultimo elemento del string
#si colocamos un indice que no existe se obtendrá un error
print(primeraLetra)
print(ultimaLetra)
print(penultimaLetra)
#podemos generar substrings
subStringConSaltos = texto[1:7:2] #obtener los elementos a partir del indice:hasta:saltos
print(subStringConSaltos)


