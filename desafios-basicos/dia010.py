# Gerador de Senhas
# Crie uma função que gere senhas aleatorias de 8 caracteres
import string
import random
import time

letras_maiusculas = list(string.ascii_uppercase)
letras_minusculas = list(string.ascii_lowercase)

numeros = list(map(str, range(10)))

sinais_especiais = list("!@#$%^&*()-_=+[]{}|;:',.<>?/`~")

senhas_db = letras_maiusculas + letras_minusculas + numeros + sinais_especiais

def gerador_senhas():
  senha = ""
  contador = 0

  while contador <= 8:
    id = random.choice(senhas_db)
    senha += id
    contador += 1
  
  print(f"Gerando senha ...")

  print(f"\nA sua nova senha é : {senha}")
  

print("Hello World ! Eu sou um programa gerador de senhas.")

gerador_senhas()
