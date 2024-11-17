# Calculadora de IMC
# Crie um programa para calcular o indice de massa corporal.
# imc = peso / altura ** 2

def calcular_imc(peso, altura):
  imc = peso / (altura ** 2)
  
  print(f"\nO seu IMC é {imc:.2f}, e para um adulto você está ", end="")

  if imc < 18.5:
    print("abaixo do peso, recomenda-se ir ao nutricionista.")
  elif imc <= 25:
    print("com o peso normal, não é motivo para preocupação.")
  elif imc <= 30:
    print("com sobrepeso, recomenda-se ir ao nutricionista.")
  elif imc <= 35:
    print("com obesidade grau 1, recomenda-se ir ao médico, quando possivel.")
  elif imc < 40:
    print("com obesidade grau 2, recomenda-se ir ao médico urgentimente !!!")
  elif imc >= 40:
    print("com obesidade grau 3, recomenda-se ir ao médico AGORA!!.")
  
  print("\nEsta é apenas uma estimativa, em qualquer situação procure um nutricionista e cuide da sua saúde.")
  

print("Hello World ! Eu sou um programa python para calculo de IMC.\n")
print(
  " O Indice de Massa Corporal ou IMC, é uma medida usada para avaliar se uma pessoa\n",
  "está dentro do peso ideal para sua altura. Ele é amplamente utilizado como um indicador\n",
  "de saude relacionado ao peso, embora tenha suas limitações, pois não leva em consideração\n",
  "a composição corporal(massa muscular, gordura, etc).\n"
)

peso = float(input("Informe seu peso : "))
altura = float(input("Informe sua altura : "))

calcular_imc(peso, altura)
