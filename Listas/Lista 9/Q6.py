'''6) Escreva um algoritmo que imprima a lista dos números primos entre 200 e 300. Número primo é um número natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição, 1 não é primo.'''

print("Os números primos de 200 a 300:")

numeros_primos = []

for numero in range(200, 301):
    tag_de_primo = True
  
    for n in range(2, numero):
      if numero % n == 0:
        tag_de_primo = False
  
    if tag_de_primo == True:
        numeros_primos.append(numero)

for primo in numeros_primos:
    print(primo)