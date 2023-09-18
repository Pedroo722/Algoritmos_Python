'''8) Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4 × 5 × 6 = 120. Escreva um algoritmo que imprima os números triangulares entre 300 e 500.'''

print("O números triangulares de 300 a 500 são:")

for x in range(300,501):
  produto = 1
  i = 1
  
  while produto < x:
      produto = i * (i + 1) * (i + 2)
      if produto == x:
          print(f"{x} é um número triangular.")
      i += 1



'''
Tinha achado o resultado estranho, então fiz os cálculos manualmente.
336 é mesmo o único numero triangular no intervalo de 300 a 500.

5 * 6 * 7 = 210
6 * 7 * 8 = 336
7 * 8 * 9 = 504
'''