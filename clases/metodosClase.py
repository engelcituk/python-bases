
class Circulo:
  pi = 3.14159265

  @classmethod # se usan metodos de clase cuando se requieren usar variables de clase
  def area(cls, radio): #por convencion se usa cls, para los metodos de clase, hace referencia a la clase
    return cls.pi * radio**2 #pi por radio al cuadrado

resultado = Circulo.area(10)
print(resultado)