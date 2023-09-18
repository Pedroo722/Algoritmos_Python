# Escreva um algoritmo para a operacão de saque de um caixa eletrônico. Ele deve ler um número inteiro correspondendo ao valor a ser sacado e deve retornar quais cédulas o caixa entregaria. O número mínimo de cédulas deve ser entregue. Considere que não faltam cédulas e que estão disponíveis as cédulas de 50 e 10.

Saque = int(input())

# Notas de 50
notas_50 = Saque // 50
sobra1 = Saque % 50

# Notas de 20
notas_20 = sobra1 // 20
sobra2 = sobra1 % 20

# Notas de 10
notas_10 = sobra2 // 10
sobra3 = sobra2 % 10


# Notas Sacadas
print("O total sacado será:")
print(notas_50, "notas de 50R$")
print(notas_20, "notas de 20R$")
print(notas_10, "notas de 10R$")