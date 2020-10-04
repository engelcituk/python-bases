lenguajes = "Python; Php; Java; C; C#; Rubi; Swift; Javascript"

separador = "; " #sin espacios ni puntos y coma
resultado = lenguajes.split(separador) #retorna una lista del texto

nuevoString  = " ".join(resultado) ##genero un string con los elementos de la lista
stringOriginal = separador.join(resultado)#para regresar al string original

print(resultado)
print(nuevoString)
print(stringOriginal)

texto = """ Este es un texto
con saltos
de linea """

stringSinSaltos = texto.splitlines()
print(stringSinSaltos)
