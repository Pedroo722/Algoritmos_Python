# Escreva um algoritmo que recebe como entrada uma data no formato dd/mm/aaaa e, em seguida, escreva a data por extenso. Por exemplo, se receber 07/03/2016 dever ́a escrever “07 de Março de 2016”.

print("Digite sua data no formato dd/mm/aaaa:")
print("(Exemplo: 05/07/2019)")

data = input()
dia, mes, ano = data.split("/")

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

print(f"{dia} de {meses[int(mes)-1]} de {ano}")