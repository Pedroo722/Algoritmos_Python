'''5) Escreva um algoritmo que imprima a lista dos 100 primeiros números primos, iniciando do 2. Número primo é um número natural que tem apenas dois divisores diferentes, o 1 e ele mesmo. Por definição, 1 não é primo.'''

print("Os 100 primeiros números primos:")

numeros_primos = [2, 3]
numero_atual = 4

while len(numeros_primos) < 100:
    tag_de_primo = True
    
    for n in numeros_primos:
      if numero_atual % n == 0:
          tag_de_primo = False
    
    if tag_de_primo == True:
      numeros_primos.append(numero_atual)
    
    numero_atual += 1

for primo in numeros_primos:
    print(primo)
