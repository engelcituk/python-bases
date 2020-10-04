class Animal: #las clases padres que tendrán hijos deben de ir en la parte superior de todo el script
  def comer(self):
    print("Comiendo")

  def dormir(self):
    print("Durmiendo")

class Mascota:
  def fecha_adopcion(self, fecha):
    self.fecha_de_adopcion = fecha

#clase usando herencia multiple, separados por comas
class Perro(Animal, Mascota): #para que una clase herede de otra se pone () y entre ella poner el nombre de la clase del cual hereda
  def __init__(self, nombre):
    self.nombre = nombre

  def ladrar(self):
    print("Ladrando")

  def dormir(self): #Sobre escritura de métodos
    print(self.nombre, "esta durmiendo!")
    Animal.dormir(self) #para añadir más funcionalidades al metodo padre
    print("No molestar") #sobreescribir metodo 
    
firulais = Perro("Firulais")
firulais.dormir()