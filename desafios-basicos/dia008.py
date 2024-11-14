# Fatorial
# Calcule o fatorial de um número

def calcular_fatorial(numeros = 5):
    fatorial = 1

    print("\nO resultado do cálculo fatorial é:")
    
    for numero in range(numeros, 0, -1):
        fatorial *= numero

        print(f"FATORIAL : {fatorial}")

print("OLA MUNDO!\nMinha função Python é calcular o fatorial de um número")

numero = int(input("Informe o número que deseja calcular: "))

calcular_fatorial(numero)
