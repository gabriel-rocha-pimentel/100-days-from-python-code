# Cálculo de Soma
# Receba dois números e imprima a soma deles.
start = "SIM"

while start[0] == "S":
  print("Farei a soma de dois números e mostrarei o resultado.")

  a = int(input("Por favor insira o primeiro número : "))
  b = int(input("Por favor insira o segundo número : "))

  soma = a + b

  print(f"A soma de {a} mais {b} é : {soma}")

  start = str(input("\nQuer continuar ? Sim ou Não\n>>>\t")).upper()

  if start[0] != "N":
    print("Por favor, insira [NÃO] para parar o programa !")
    