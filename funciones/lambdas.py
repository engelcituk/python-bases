
def centigradosAFarhenheit(grados):
    return grados * 1.8 + 32

funcionVariable = centigradosAFarhenheit
grados = funcionVariable(32)
print(grados)

#funciones lambda o funciones anonimos, realizan tareas muy pequeñas, refactorizamos lo anterior a una funcion lambda
mi_funcion = lambda grados=0 : grados * 1.8 + 32 #lambda parametros: return o la operacion a realizar, no se pone return porque siempre regresan algo

resultado = mi_funcion(32)
print(resultado)