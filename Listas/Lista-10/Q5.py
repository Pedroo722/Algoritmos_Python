'''5) Escreva um algoritmo que leia uma string e escreva como saída o caracter que mais ocorre e o número de ocorrências deste.'''


frase = input("Digite alguma coisa: ")
caractere = ""
ocorrencias = 0

for c in frase:
  if c != " ": # ignorar os espaços
    contador = frase.count(c)
    if contador > ocorrencias:
        ocorrencias = contador
        caractere = c


print(f'O caractere mais comum é: "{caractere}". \nTendo ocorrido {ocorrencias} vezes')     