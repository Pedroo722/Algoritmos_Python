'''5) Escreva um algoritmo que leia uma palavra e a escreva invertida. Ex.: ao ler IFPB, escreve
BPFI.'''

frase = input("Digite uma palavra: ")
invertida = ""

for c in frase:
  invertida = c + invertida

print(invertida)