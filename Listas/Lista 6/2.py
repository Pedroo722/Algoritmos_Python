'''
2) Escreva um algoritmo que receba como entrada um mês do ano (Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro) e indique o número de dias no mês. Considere Fevereiro sempre com 28 dias. Utilize a estrutura match e agrupe os meses com mesma quantidade de dias.
'''

mes = input("Digite um mês: ")

match mes:
  case "Fevereiro":
    print("O mês tem 28 dias")
  case "Abril" | "Junho" | "Setembro" |"Novembro":
    print("O mês tem 30 dias")
  case _:
    print("O mês tem 31 dias")