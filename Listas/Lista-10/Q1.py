'''1) Escreva um algoritmo que imprima os números de 300 a 500, mas não deve imprimir os múltiplos de 25. Utilize o comando continue obrigatoriamente.'''

print("Números de 300 a 500. Sem os múltiplos de 25:")

for i in range(300, 501):
  if i % 25 == 0:
    continue
  print(i)