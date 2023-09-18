'''
Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4 × 5 × 6 = 120. Escreva um algoritmo que imprima os 10 primeiros números triangulares.
'''

print("Os 10 primeiros números triangulares são:")

for n in range(0,11):
  valor = n * (n+1) * (n+2)
  print(valor)