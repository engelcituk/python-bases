texto = "este es una cadena de textO"

resultado = texto.capitalize();#pone en mayuscula la primera letra de un string
resultado2 = texto.swapcase();#convierte todo el texto que está en mayusculas a minusculas y viceversa
resultado3 = texto.upper();#convierte todo el texto que está en mayusculas
resultado4 = texto.lower();#convierte todo el texto que está en minusculas
resultado5 = texto.title();#genera un string con un formato de titulo
resultado6 = texto.replace("textO", "string", 1 );#(valor a reemplazar, el reemplazo, el 3er argumento es para indicar las veces del reemplazo)

texto2 = " este es una cadena de texto "
resultado7 = texto2.strip();#eliminar espacios al principio y al final


print(resultado)
print(resultado2)
print(resultado3,'Son mayusculas:', resultado3.isupper())
print(resultado4, 'Son minusculas:', resultado4.islower())
print(resultado5)
print(resultado6)
print(resultado7)


