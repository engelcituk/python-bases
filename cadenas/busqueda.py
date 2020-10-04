mensaje = "Unfeeling so rapturous discovery impression he exquisite. Reasonably so middletons or impression by terminated. Old pleasure required removing elegance him had."

resultado = mensaje.count('impression')#si el texto que se busca no se encuentra count regresa un 0
resultado2 = "impression" in mensaje # otra forma de buscar, pero este regresa un booleano
resultado3 = "impression" not in mensaje # otra forma de buscar negando
resultado4 = mensaje.find('impression')#si el texto que se busca se encuentra, se regresa la posicion del primer string encontrado, sino retorna un -1

resultado5 = mensaje[ resultado4: resultado4 + len("impression") ]# [33: 33+10] ->>>>> [33:43]

resultado6 = mensaje.startswith('Unfeeling')#Para ver si al principio de la cadena empieza con Unfeeling, se regresa un booleano
resultado7 = mensaje.endswith('had')#Para ver si al final de la cadena termina con had, se regresa un booleano


print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print(resultado5)
print(resultado6)
print(resultado7)




