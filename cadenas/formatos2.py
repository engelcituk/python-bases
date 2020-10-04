llora = "miau"
gato = "michi dice"

resultado = "Mi super %s %s" %(gato, llora)
resultado2 = "Mi super {} {}".format(gato, llora)
resultado3 = "Mi super {a} {b}".format(a = gato, b = llora) #mejora de la linea anterior, permitiendo asi usarlo respecto al nombre y no por la posicion


print(resultado)
print(resultado2)
print(resultado3)

