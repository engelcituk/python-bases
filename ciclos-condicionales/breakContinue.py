titulo = "Holis"
titulo2= "Hola mundo"


for caracter in titulo:
  if caracter == "l":
    break
  print(caracter)


print("\n")

for caracter in titulo:
  if caracter == "m":
    continue
  print(caracter)