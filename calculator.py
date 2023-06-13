def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

result = None
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

while True:
    if result is None:
        print(logo)
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

    choice = input(f"Deseja continuar com {result} ou voltar ao menu? YES para continuar NO para voltar ao menu\nYES \nNO\n: ")
    choice = choice.upper()

    while choice != "YES" and choice != "NO":
        choice = input("Escolha inválida. Digite YES para continuar ou NO para voltar ao menu\nYES \nNO\n: ")
        choice = choice.upper()

    if choice == "NO":
        result = None
        continue
