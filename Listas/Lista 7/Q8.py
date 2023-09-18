'''Escreva um algoritmo que leia dois números, limite inferior e limite superior, some e imprima o quadrado, (x^2), de todos os números de limite inferior a limite superior. Por exemplo, se o usuário digitar 2 como limite inferior e 5 como limite superior, deve imprimir 54.'''

a = int(input())
b = int(input())

soma = 0

for n in range(a,b+1):
  quadrado = n ** 2
  soma = soma + quadrado
  
print(soma)