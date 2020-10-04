#Llamaremos closure cuando una funcion genere dinamicamente otra funcion
def mostrar_mensaje(mensaje):
  mensaje = mensaje.title() #local
  
  def mostrar():
    print(mensaje)

  return mostrar #retorna la funcion mostrar


nueva_funcion = mostrar_mensaje("CodigoFacilito")
nueva_funcion()