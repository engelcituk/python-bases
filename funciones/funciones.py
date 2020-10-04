def saluda():
    print('hola mundo')

saluda()

def crearMensaje(nombre):
    return 'Hola {}, Bienvenido al curso de Python 3'.format(nombre)

print(crearMensaje('Juanito'))

def suma(valor1, valor2, valor3, valor4):
    return valor1 + valor2 + valor3 + valor4

print(suma(1,2,3,4))

def getCourse():
    return 'Curso de Python', 'super', 3.8

curso, nivel, version  = getCourse()
print(curso, nivel, version)