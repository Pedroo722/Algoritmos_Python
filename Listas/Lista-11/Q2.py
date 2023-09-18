'''2) Um número par é um número inteiro que pode ser escrito na forma 2n e n é inteiro. Escreva uma função que receba um inteiro e retorne se ele é par ou não. Em seguida escreva um programa que leia números inteiros e indique se é par ou não, usando a função. O programa deve ser encerrado quando a entrada for -1.'''

def par(a):
  if a % 2 == 0:
    print(f"O número {a} é par.")
  else:
    print(f"O número {a} não é par.")


while True:
  numero = int(input("Digite um número: "))
  if numero == -1:
    print("O processo foi interrompido porque as duas entradas são 0.")
    break
  par(numero)