# Sobre Palindromos
# Crie uma função que verifica se uma palavra é um palindromo

print("Hello Wold, eu sou um programa python!")
print("Minha função é descobrir palindromos.")

def detector_palindromo(frase):
  contando = 0
  palavras = frase.split()

  for palavra in palavras:
    palavra.lower()
    nova_palavra = palavra.replace(",", "")
    palavra_inversa = nova_palavra[::-1]

    if palavra_inversa == nova_palavra:
      contando += 1
  
  print(f"\nVocê tem um total de {contando} palindromos na frase:\n- {frase}.")

palavra = str(input("Por favor, escreva uma frase e descobrirei o palindromo: "))

detector_palindromo(palavra)
