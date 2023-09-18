# Escreva um algoritmo que leia um ano e, em seguida, informe se este ano  é ou não bissexto.

Ano_atual = int(input("Digite algum ano para verificar se ele é ou não bissexto: \n"))

if (Ano_atual % 4 == 0 and Ano_atual % 100 != 0) or (Ano_atual % 400 == 0):
    print(f"O ano de {Ano_atual} é bissexto.")
else:
    print(f"O ano de {Ano_atual} não é bissexto.")