# Contagem Regressiva
# Implemente uma contagem regressiva de 10 a 0
import time

def contagem_regressiva():
  start = int(input("Insira o número de ínicio da contagem : "))

  print("\nComeçando em", end=" ")
  
  for numero in range(start, 0, -1):
    print(f"{numero}", end=" ")
    time.sleep(0.5)
  
  print("\nFIM")

print("Hello World ! Eu sou uma programa em pyhton de contagem regressiva.")

contagem_regressiva()
