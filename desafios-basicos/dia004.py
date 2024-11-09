# Número par ou ímpar
# Verifique se um número é par ou ímpar

print("Na matemática, os números pares são aqueles divisiveis por dois.")

start = "SIM"

while start[0] == "S":
  print("\nDigite um número e eu farei o calculo para determinar, se ele é par ou ímpar")
  numero = int(input("Número : "))

  if numero % 2 == 0:
    print(f"O {numero} é PAR")
  else:
    print(f"O {numero} é ÍMPAR")

  start = str(input("\nQuer continuar ? Sim ou Não\n>>>\t")).upper()

  if start[0] != "N":
    print("Por favor, insira [NÃO] para parar o programa !")
