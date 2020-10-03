variableUno = 10
variableDos = 18

#Los operadores relacionales

mayor = variableUno > variableDos
menor = variableUno < variableDos 
mayor_igual = variableUno >= variableDos 
menor_igual = variableUno <= variableDos 
igual = variableUno == variableDos 
igual2 = variableUno is variableDos #tambien se pueden comparar si dos valores enteros son iguales con la palabra reservada is

diferente = variableUno != variableDos 

# print(mayor)
# print(menor)
# print(mayor_igual)
# print(menor_igual)
# print(igual)
# print(diferente)

#Los operadores logicos
resultadoAnd = True and True and diferente; #True con la T en mayuscula, todas deben ser verdadero para que el resultado sea true, o todos deber ser 
resultadoOR = True or True or diferente; #por lo menos una de las condiciones debe ser verdadero para que el resultado sea verdadero
resultadoNot = not False; 
resultadoNot = not True; 


print(resultadoAnd)
print(resultadoOR)
print(resultadoNot)
print(igual2)





