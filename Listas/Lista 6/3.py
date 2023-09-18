'''
3) Escreva um algoritmo que receba um inteiro entre 1 e 7 e indique o dia da semana. Considere 1 sendo Domingo e 7 sendo Sábado. Utilize match.
'''

numero = int(input("Digite um número de 1 a 7 representando o dia da semana: "))
print("(A semana começa no Domingo - 1)")

match numero:
  case 1:
    print("O dia da semana é domingo.")
  case 2:
    print("O dia da semana é segunda.")
  case 3:
    print("O dia da semana é terça.")
  case 4:
    print("O dia da semana é quarta.")
  case 5:
    print("O dia da semana é quinta.")
  case 6:
    print("O dia da semana é sexta.")
  case 7:
    print("O dia da semana é sábado.")
  case _:
    print("Isso não é um dia da semana válido.")