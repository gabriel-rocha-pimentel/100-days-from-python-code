# Números Primos
# Crie uma função que identifique se um número é primo ou não
import math

print("Hello world! Eu sou um programa em python !")
print("Minhas função é identificar se o número fornecido é primo ou não.\n")
print("Mas o que é um número primo ?\n")
print(
  "Um número primo é um número natural maior que 1\nque só pode ser dividido por 1 e por ele mesmo, sem deixar resto."
)

def identificador(numero_escolhido):
  numeros_divisiveis = []

  if numero_escolhido > 1:
    limite = round(math.sqrt(numero_escolhido))
    
    for numero in range(2, limite + 1):
      if (numero_escolhido % numero) == 0:
        numeros_divisiveis.append(numero)
      
  else:
    print("POR FAVOR INSIRA UM NÚMERO POSITIVO!")
  
  if not numeros_divisiveis:
    print(f"\nO número {numero_escolhido} é um número primo")
  else:
    print(f"\nO número {numero_escolhido} não é um número primo")

numero = int(input("\nInsira um número para identificar : "))

identificador(numero)
