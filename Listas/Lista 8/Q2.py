'''2) Escreva um algoritmo que leia uma palavra e escreva o número de cada uma das vogais.'''

frase = input("Digite uma palavra: ").upper()

A = frase.count("A")
B = frase.count("B")
C = frase.count("C")
D = frase.count("D")
E = frase.count("E")

print(f'A vogal "A" apareceu {A} vezes')
print(f'A vogal "B" apareceu {B} vezes')
print(f'A vogal "C" apareceu {C} vezes')
print(f'A vogal "D" apareceu {D} vezes')
print(f'A vogal "E" apareceu {E} vezes')