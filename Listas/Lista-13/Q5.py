'''5) Escreva um algoritmo que leia 10 nomes e os escreva em ordem alfabética.'''

lista = []

contador = 0
while contador < 10:
  nome = input()
  lista.append(nome)
  contador += 1


lista.sort()
l2 = list(map(lambda x: x.capitalize(), lista))

print("Lista dos nomes ordem alfabética: ")
print(l2)
