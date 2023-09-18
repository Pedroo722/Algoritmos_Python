'''3) Escreva um algoritmo que imprima um menu com cinco opções (soma, subtração, multiplicação, divisão e sair) e, de acordo com a escolha do usuário, deve solicitar os dois operandos e realizar a operação ou encerrar a execução. Enquanto não escolher sair, o algoritmo deve ficar imprimindo o menu, lendo a opção e executando a operação aritmética.'''

print("Escolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Sair")

op = input()

while op != "5" and op != "Sair":
  # Entrada de números
  
  n1 = float(input("Digite um número: "))
  n2 = float(input("Digite um segundo número: "))

  # Operações
  
  if op == "1" or op == "Soma":
    resultado = n1 + n2
    print(f"Resultado: {resultado} \n")
  elif op == "2" or op == "Subtração":
    resultado = n1 - n2
    print(f"Resultado: {resultado} \n")
  elif op == "3" or op == "Multiplicação":
    resultado = n1 * n2
    print(f"Resultado: {resultado} \n")
  elif op == "4" or op == "Divisão":
    resultado = n1 / n2
    print(f"Resultado: {resultado} \n")
  else:
    print()
    print(f'Espere! "{op}" não é uma operação válida. \n')

  # Tabela e entrada de operação 
  
  print("Escolha uma operação:")
  print("1 - Soma")
  print("2 - Subtração")
  print("3 - Multiplicação")
  print("4 - Divisão")
  print("5 - Sair")

  op = input()

# fim

print("A execução foi encerrada.")
