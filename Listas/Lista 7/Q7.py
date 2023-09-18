'''Um número par é um número inteiro que pode ser escrito na forma 2n e n é inteiro. Escreva um algoritmo que escreva a soma dos 100 números pares consecutivos, iniciando do 100.'''

soma = 0

for n in range(100,201,2):
  soma = soma + n
  
print(f"A soma dos 100 numeros pares consecultivos, iniciando de 100, é igual a {soma}")
