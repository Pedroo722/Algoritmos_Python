'''1) Escreva um algoritmo que realize somas consecutivas de dois números reais. Ele deve ser encerrado quando receber duas entradas iguais a 0.'''


n1 = int(input())
n2 = int(input())

while n1 != 0 or n2 != 0:
  print(n1+n2)
  n1 = int(input())
  n2 = int(input())

print("O processamento encerrou porque os dois valores são iguais a 0.")
