# Área de um Círculo
# Crie uma função que calcule a área de um circulo com um raio dado
import math

print("Eu farei o calculo da área de um circulo para você\n")

def calcule_area():
  raio = int(input("Primeiro informe o raio do cículo : "))
  area = math.pi * raio ** 2

  print(f"A área de um circulo com um raio de {raio} é : {area}.")

calcule_area()
calcule_area()