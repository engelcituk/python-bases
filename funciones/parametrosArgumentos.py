def crearUsuario(nombre, apellido, edad=28): #tabien se puede poner valores por defecto, la asignacion sin espacios como recomendacion
    return {
        'nombre' : nombre,
        'apellido': apellido,
        'nombre_completo' : "{} {}".format(nombre, apellido),
        'edad': edad
    }

#codi = crearUsuario('Codi', 'Easy', 56) #si falta un argumento se genera un error, a menos que en la funcion existe un valor por default
codi = crearUsuario( edad=11, apellido='Facilito', nombre='Codi') # asignacion mediante el nombre de los parametros, asi no es necesario seguir un orden

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])