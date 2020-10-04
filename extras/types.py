#las anotaciones son de caracter unicamente informativo
#los tipos de datos con los que podemos trabajar son: str,int, float y bool

#saludo recibe como parametro nombre de tipo string y que no regresa nada la funcion 
def saludo(nombre: str) -> None: #la flecha indica el tipo de dato que retorna la funcion
    print("Hola "+ nombre)

nombre = "Lucy"
saludo(nombre)

def suma(numero1: int, numero2: int = 100) -> int: #recibo enteros y retorno un entero, uno de los parametros tiene un valor por default
    return numero1 + numero2

print( suma(10) )