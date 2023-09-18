'''6) Escreva um algoritmo que leia 10 números e os escreva em ordem decrescente.'''

lista = []

contador = 0
while contador < 10:
  n = int(input())
  lista.append(n)
  contador += 1

l2 = sorted(lista, reverse=True)

print("Lista desorganizada: ")
print(lista)

print("Lista organizada: ")
print(l2)
