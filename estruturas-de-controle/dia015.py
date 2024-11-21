# Soma de Números Pares
# Some números pares de uma lista fornecida

print("Hello World! Eu sou um programa python de soma")
print("\nEu fui criado para fazer a soma de uma lista de números pares.")

entrada = input("Insira os números que precisa somar com uma ',' : ")

lista_numerada = list(map(int, entrada.split(",")))

numeros_pares = []

for numero in lista_numerada:
  if (numero % 2) == 0:
    numeros_pares.append(numero)

numero_par = 0

for numero in numeros_pares:
  numero_par += numero

print(f"\nOs números pares de sua lista são {numeros_pares} é a soma de todos é {numero_par}")
