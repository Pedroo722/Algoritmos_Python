'''5. A função fatorial é defina da seguinte forma: n! = n × (n − 1)!. Escreva uma função que receba um número inteiro e retorne o seu fatorial. Em seguida escreva um programa que leia um inteiro e, usando a função, calcule e escreva o seu fatorial.'''

def fatorial(a):
  resultado = 1
  for i in range(1, a+1):
    resultado *= i
  return resultado


numero = int(input("Digite um número: "))
fatorial = fatorial(numero)
print(f"A fatorial de {numero} é igual a: {fatorial}")