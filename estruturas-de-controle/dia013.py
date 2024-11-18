# Tabela de Multiplicação
# Exiba a tabela de multiplicação de 1 a 10

print("Hello World ! Está é a tabela de multiplicação.")

print("---------------------------------------------------- TABUADA ----------------------------------------------------")
for lugar in range(0, 11):
  for numero in range(0, 11):
    print(f"{lugar} X {numero} = {lugar * numero}", end="\t")

  print()
