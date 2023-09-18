'''4. Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4 × 5 × 6 = 120. Crie uma função que indica se um número é triangular ou não. Em seguida escreva um programa que leia números inteiros e indique se é triangular ou não, usando a função. O programa deve ser encerrado quando a entrada for -1.'''

def triangular(a):
  i = 0
  while i * (i + 1) * (i + 2) < a:
    i += 1
  if i * (i + 1) * (i + 2) == a:
    print(f"{a} é um número triangular.")
  else:    
    print(f"{a} não é um número triangular.")

while True:
  numero = int(input("Digite um número: "))
  if numero == -1:
    print('O programa foi encerrado porque o valor dado é igual a "-1"')
    break
  triangular(numero)