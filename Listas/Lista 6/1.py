'''
1) Reescreva o algoritmo que lê um inteiro e indica se é positivo, neutro ou negativo, usando Expressão Condicional.
'''

numero = int(input("Digite um número: "))

if numero > 0:
  print("O numero é positivo.")
elif numero == 0:
  print("O numero é neutro.")
else:
  print("O numero é negativo.")
