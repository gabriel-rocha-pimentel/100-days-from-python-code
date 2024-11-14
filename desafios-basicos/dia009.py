# Contagem de Vogais
# Receba uma string e conte quantas vogais existem nela

def contar_vogais(palavra = "Hello Word"):
  palavra.lower()
  contar_vogal = 0
  lista_vogais = ['a', 'e', 'i', 'o', 'u']

  for letra in palavra:
    for vogal in lista_vogais:
      if letra == vogal:
        contar_vogal += 1
  
  return print(f"O número de vogais na sua palavra é {contar_vogal}")

print("Hello World ! \nEu sou um programa com a função de contar vogais")

palavra = str(input("\nPor favor insira uma palavra :\t"))

contar_vogais(palavra)
