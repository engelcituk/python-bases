
for valor in range(1,5): #imprime numeros de 1 hasta el rango 5, 
    print(valor)

print("\n")


for valor in range(1,50, 3): #imprime numeros de 1 hasta el rango 50, con saltos de 3, 
    print(valor)

print("\n")


lista = [1,2,3,4,5,6]
for ind, val in enumerate(lista, 10):
  print("índice:", ind, "valor:", val)