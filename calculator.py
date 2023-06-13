def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

result = None

while True:
    if result is None:
        n1 = int(input("Escolha o primeiro número: "))
        n2 = int(input("Escolha o segundo número: "))
    else:
        n1 = result
        n2 = int(input("Escolha o próximo número: "))

    operation = input("Escolha a operação:\n+\n-\n*\n/\nS para sair\n:")
    operation = operation.upper()

    if operation == "+":
        result = add(n1, n2)
    elif operation == "-":
        result = subtract(n1, n2)
    elif operation == "*":
        result = multiply(n1, n2)
    elif operation == "/":
        result = divide(n1, n2)
    elif operation == "S":
        break
    else:
        print("Operação inválida")
        continue

    print("Resultado:", result)

    choice = input(f"Deseja continuar com {result} ou voltar ao menu?\nYES para continuar\nNO para voltar ao menu ")
    choice = choice.upper()

    while choice != "YES" and choice != "NO":
        choice = input("Escolha inválida. Digite YES para continuar ou NO para voltar ao menu: ")
        choice = choice.upper()

    if choice == "NO":
        result = None
        continue
