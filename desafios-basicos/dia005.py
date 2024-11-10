# Calculadora Simples
# Crie uma função que execute as operações básicas,
# Adição, Subtração, Multiplicação, Divisão

def calculadora(numero1 = 1, numero2 = 1, sinal_operacao = "+"):
  int(numero1)
  int(numero2)
  str(sinal_operacao)

  if sinal_operacao == "+":
    resultado = numero1 + numero2
    print(f"A soma de {numero1} mais {numero2} é : {resultado}")
  
  elif sinal_operacao == "-":
    resultado = numero1 - numero2
    print(f"A subtração de {numero1} menos {numero2} é : {resultado}")
  
  if sinal_operacao == "*":
    resultado = numero1 * numero2
    print(f"A multiplicação de {numero1} com {numero2} é : {resultado}")
  
  if sinal_operacao == "//":
    resultado = numero1 // numero2
    print(f"A divisão de {numero1} por {numero2} é : {resultado}")

#Adição
calculadora(5, 5, "+")
#Subtração
calculadora(5, 5, "-")
#Multiplicação
calculadora(5, 5, "*")
#Divisão
calculadora(5, 5, "//")