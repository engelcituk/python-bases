class Triangulo:

  numero = 2

  @staticmethod # para tranformar el método en estatico, los métodos estaticos no requieren de instancia
  def area(base, altura):
    return (base * altura) / Triangulo.numero

resultado = Triangulo.area(10, 20)
print(resultado)