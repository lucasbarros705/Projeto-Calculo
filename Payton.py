# soma.py

def somar(a, b):
    return a + b

# Programa principal
if __name__ == "__main__":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = somar(num1, num2)
        print(f"A soma de {num1} + {num2} = {resultado}")
    except ValueError:
        print("Por favor, digite apenas números válidos.")