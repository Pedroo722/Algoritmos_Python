'''3) Número primo é um número natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição, 1 não é primo. Crie uma função que indica se um número é primo ou não. Em seguida escreva um programa que leia números inteiros e indique se é primo ou não, usando a função. O programa deve ser encerrado quando a entrada for -1.'''

def primo(a):
  contador = 0
  i = 0
  while i <= a or contador < 2:
    i = i + 1
    divisao = a % i
    if divisao == 0:
      contador = contador + 1
  if contador <= 2:
    print("O número é primo")
  else:
    print("O número não é primo")
    
while True:
  numero = int(input("Digite um número: "))
  if numero == -1:
    print('O programa foi encerrado porque o valor dado é igual a "-1"')
    break
  primo(numero)