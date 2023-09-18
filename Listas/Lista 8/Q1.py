'''1) Escreva um algoritmo que leia uma palavra e indique o número de ocorrências de cada uma das seguintes letras, B, C e D.'''

frase = input("Digite algo: ")

B = frase.count("B")
C = frase.count("C")
D = frase.count("D")

print(f'A letra "B" apareceu {B} vezes')
print(f'A letra "C" apareceu {C} vezes')
print(f'A letra "D" apareceu {D} vezes')
