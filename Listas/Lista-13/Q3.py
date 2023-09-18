'''3) Escreva um algoritmo que imprima a lista dos 100 primeiros números primos, iniciando do 2. Número primo é um número natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição, 1 não é primo. Crie e utilize uma função que indica se um número é primo ou não e mantenha os números primos em uma lista. Imprima, ao final, a soma dos 100 números primos impresso. Para isso, crie uma função chamada soma que receba a lista como parâmetro e retorne a soma.'''

def primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def soma(lista):
  soma = 0
  for i in lista:
    soma += i
  return soma


numeros_primos = []
contador = 0
numero = 2

while contador < 100:
    if primo(numero):
        numeros_primos.append(numero)
        contador += 1
    numero += 1
  
print(f"Lista dos 100 primeiros números primos: \n\n{numeros_primos}")

soma = soma(numeros_primos)
print(f"\nSoma dos 100 primeiros números primos: {soma}")