'''6. A série de Fibonacci tem 1 como primeiro e segundo elemento. A partir daí, a série segue definindo o próximo valor como a soma dos dois anteriores. Por exemplo, o terceiro elemento da série é 2 e o quarto é 3. Os oito primeiros elementos são 1, 1, 2, 3, 5, 8, 13 e 21. Escreva uma função que receba um número inteiro, i, e retorne o i-ésimo elemento da série. Em seguida escreva um programa que leia números inteiros e indique os i-ésimos números da série, usando a função. O programa deve ser encerrado quando a entrada for -1.'''

def serie(i):
  if i == 1 or i == 2:
    return 1
  else:
    a, b = 1, 1
    for x in range(i - 2):
      a, b = b, a + b
    return b

while True:
  numero = int(input("Digite um número: "))
  resultado = serie(numero)
  if numero == -1:
    print('"O processamento foi encerrado porque a entrada é igual a "-1"')
    break
  else:
      print(f"O {numero}-ésimo número da série de Fibonacci é: {resultado}")