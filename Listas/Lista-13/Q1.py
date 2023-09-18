'''1) Escreva um algoritmo que leia 30 números inteiros e os armazene em uma lista. Escreva as funções maior, menor e soma. Elas devem receber a lista e retornar o respectivo valor. Por fim, faça chamadas ás funções e imprima os retornos.'''

def soma(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma


def maior(lista):
  maior = None
  for i in lista:
    if maior == None or i > maior:
      maior = i
  return maior


def menor(lista):
  menor = None
  for i in lista:
    if menor == None or i < menor:
      menor = i
  return menor


lista = []
contador = 0

while contador < 30:
  n = int(input())
  lista.append(n)
  contador += 1

maior = maior(lista)
menor = menor(lista)
soma = soma(lista)

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Soma de todos os elementos: {soma}")