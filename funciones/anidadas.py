

def comenzar_play_list(lista):

  def reproducir():
    #nonlocal lista #para modificar las variables locales
    lista = [1,2,3]
    for val in lista:
      print(val)

  reproducir()# dentro de la funcion principal llamo a la funcion
  print(lista)

lista = ['track 1', 'track 2', 'track 3', 'track 4']
comenzar_play_list(lista)