'''
4) Escreva um algoritmo que receba um inteiro entre 1 e 7, representando o dia da semana, e indique se dia útil ou final de semana. Considere 1 sendo Domingo e 7 sendo Sábado. Utilize match e agrupe os dias úteis e em outro grupo os dias de final de semana. 
'''

numero = int(input("Digite um número representando o dia da semana: "))


match numero:
  case 1 | 7: 
    print("Esse dia da semana está no final de semana")
  case 2 | 3 | 4 | 5 | 6:
    print("O dia da semana é um dia útil.")
  case _:
    print("Isso não é um dia da semana válido.")