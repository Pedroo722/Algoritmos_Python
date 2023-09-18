'''5) Escreva um algoritmo que leia 10 números inteiros e imprima, a soma deles.'''

print("Digite 10 números:")

soma = 0

for n in range(10):
  entrada = float(input())
  soma = soma + entrada

print("A soma dos 10 números é: %.2f" % soma)