'''6) Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da esquerda para a direita ou vice-versa. Por exemplo, OSSO e OVO são palíndromos. Escreva um algoritmo que leia uma palavra e indique se é palíndromo ou não.'''

palavra = input("Digite uma palava: ").upper() #upper para funcionar com palavra tipo "Ovo"

soma1 = ""
soma2 = ""

for c in palavra:
  soma1 = c + soma1

for c in palavra:
  soma2 = soma2 + c

if soma2 == soma1:
  print("É palindromo.")
else:
  print("Não é palindromo.")