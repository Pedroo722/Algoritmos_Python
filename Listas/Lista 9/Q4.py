'''4) Escreva um algoritmo que leia um número inteiro e indique se este é primo ou não. Número primo é um número natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição, 1 não é primo.'''


n = int(input("Digite um número inteiro: "))
contador = 0
i = 0

while i <= n or contador < 2:
  i = i + 1
  divisao = n % i
  
  if divisao == 0:
    contador = contador + 1

if contador <= 2:
  print("O número é primo")
else:
  print("O número não é primo")