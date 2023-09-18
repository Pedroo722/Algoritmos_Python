'''3) Escreva um algoritmo que leia 30 números inteiros e imprima, o maior, o menor, a soma e
a média deles.'''

print("Digite 30 números inteiros.")

a = None
b = None
soma = 0
media = 0

for i in range(30):
  n = int(input("Número: "))
  soma += n
  media += n

  if a == None or n > a:
    a = n
  if b == None or n < b:
    b = n

d = media / 30

print(f"O menor valor é: {a}")
print(f"O maior valor é: {b}")
print(f"A soma dos valores é igual a: {soma}")
print(f"A média dos valores é: {d}")