class Circulo:
  pi = 3.14159265 #es una variable de clase, no requiere self, se pueden usar sin necesidad de instanciar 

  def __init__(self, radio):
    self.radio = radio #es una variable de instancia, por lo que si se modifica ese cambio solo será para esa instancia, no se comparten entre instancias


circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100

print(Circulo.pi)