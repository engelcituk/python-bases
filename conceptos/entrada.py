print('¿Cual es tú nombre?')
nombre = input() #con input se puede leer lo que se ingresa por consola, y regresa un string

print('¿Cual es tú edad?')
edad = int( input() ) #convertimos el string en entero

print('¿Cual es tú peso?')
peso = float( input() ) #convertimos el string a numero flotante, se puede reducir las lineas poniendo la pregunta como argumento en input

print('¿Estas autorizado (si/no)?')
autorizado = input() == 'si' 

print('hola', nombre, '\n')
print('edad', edad)
print('peso', peso)
print('autorizado', autorizado)


"""
este es un comentario con saltos de linea
para comentar multilinea
"""