# Escreva um algoritmo que imprima um menu com quatro opções (soma, subtração, multiplicação e divisão) e, de acordo com a escolha do usuário, deve solicitar os dois operandos e realizar a operação.

print("Escolha a operação que deseja realizar:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

operação = input("Digite a opção desejada: ")


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segunda número: "))

if operação == "1" or \
operação == "+":
    resultado = num1 + num2
    operacao = "soma"
elif operação == "2" or \
operação == "-":
    resultado = num1 - num2
    operacao = "subtração"
elif operação == "3" or \
operação == "*":
    resultado = num1 * num2
    operacao = "multiplicação"
elif operação == "4" or \
operação == "/":
    resultado = num1 / num2
    operacao = "divisão"
else:
    print("Essa não é uma operação válida. Por favor verifique se houve algum erro de digitação")
    resultado = None

if resultado is not None:
    print(f"O resultado da {operacao} é: {resultado}")