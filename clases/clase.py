class Usuario:

  def __init__(self, username='', correo='', nombre=''): #init es similar a un constructor, para inicializar atributos, siempre lleva self
    self.username = username
    self.correo = correo
    self.nombre = nombre

  def saluda(self): #todos los metodos en una clases deben llevar parametro, self es por convencion, hace referencia al objeto en si
    return "Hola, soy un usuario " + self.nombre

  def mostrar_username(self):
    print(self.username)

  def mostrar_nombre(self):
    print(self.nombre)

codi = Usuario("Codi", "codi@codigofacilito.com", "Codigo")
facilito = Usuario()

resultado = codi.saluda()
print(resultado)

#print(type(codi))