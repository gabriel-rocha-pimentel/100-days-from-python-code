# Conversão de Temperatura
# Converta de celcius para fahrenheit
# Formula de Fahrenheit F=(C×1.8)+32
print("Farei um calculo para converter Celcius em Fahrenheint.\n")

start = "SIM"

while start[0] == "S":
  celcius = int(input(f"Por favor insira a temperatura atual em celcius : "))
  fahrenheit = (celcius * 1.8) + 32

  print(f"\nA conversão de {celcius} Celcius para fahrenheit é : {fahrenheit} fahrenheit")

  start = str(input("\nQuer continuar ? Sim ou Não\n>>>\t")).upper()

  if start[0] != "N":
    print("Por favor, insira [NÃO] para parar o programa !")
