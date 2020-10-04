
class Gato:
  def __init__(self, nombre): #los guiones bajos son metodos de la clase onject __ __
    self.nombre = nombre

  def __str__(self):
    return self.nombre


class Pato(object): #otra forma de crear una clase
  def __init__(self, nombre):
    self.nombre = nombre
  
  def __str__(self):
    return self.nombre

gato = Gato("Bigotes")
gato.edad = 6
pato = Pato("Lucas")

print(gato.__dict__) #para ver los atributos de nuestros objetos
print(pato.__dict__)