'''2) Escreva um algoritmo que leia dois números, limite inferior e limite superior, imprima o quadrado, x^2, de todos os números de limite inferior a limite superior e, em seguida, imprima a soma dos números impressos. Por exemplo, se o usuário digitar 2 como limite inferior e 5 como limite superior, deve imprimir 4, 9, 16 e 25 e a soma 54. Armazene os valores que serão impressos em uma lista e, para realizar a soma, crie uma função.'''

def soma(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma
  
x = int(input("Limite inferior: "))
y = int(input("Limite superior: "))

l2 = [x**2 for x in range(x,y+1)]
soma = soma(l2)

print("\nLista com os elementos elevado ao quadrado:")
print(l2)
print(f"\nSoma dos elementos: {soma}")