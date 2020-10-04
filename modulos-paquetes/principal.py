import calculadora
#from calculadora import * #hace referencia a que se va utilizar todas la funciones del modulo calculadora
#from calculadora import suma, resta, multiplicacion, division #se puede o omitir el asterisco indicando especificamente el método a ocupar

from animales.aves import Pinguino # se indica en que modulo

""" podemos hacer saltos de linea a las importaciones si estas son demasiadas y ponerlas enntre parentesis
from calculadora import (suma,
                         resta,
                         multiplicacion,
                         division) """

"""
    tambien se pueden poner alias a las importaciones:

    from calculadora import suma as adicion

    print (adicion(20, 30)) 

"""


#print (calculadora.suma(20, 30)) #otra forma de hacer un import
#print (suma(20, 30)) #otra forma de hacer un import
#print (division(30, 2)) #si se llama una funcion sin importarla en el modulo, habrá un error

print(calculadora.__name__)
print(__name__)


pinguino = Pinguino()
pinguino.nadar()

