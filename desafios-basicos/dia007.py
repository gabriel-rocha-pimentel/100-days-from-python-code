# Inverter Strings
# Receba uma palavra e retorne a palavra invertida.

def inverter_string(palavra = "Hello World"):
  palavra_invertida = palavra[::-1]

  print(f"A sua palavra é [{palavra}] e inversa é igual a\n>>>\t{palavra_invertida}.")

print(
  "Ola Mundo, eu sou um program para reverter palavras.\n",
  "Forneça uma palavra e eu retornarei ela invertida.\n"
)

palavra = str(input("Escreva a palavra que quer inverter : "))

inverter_string(palavra)