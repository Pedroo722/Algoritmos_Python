'''8) Uma molécula de DNA é composta de fitas complementares de forma que, se tivermos
uma das fitas, a outra pode ser computada pelo complemento reverso. As bases A e T
são complementares, assim como C e G. Sendo CTGCGCTAAA uma das fitas, sua fita
complementar é TTTAGCGCAG. Escreva um algoritmo que leia uma das fitas de DNA e
retorne o complemento reverso dela.'''


fita = input("Digite uma fita de mólecula de DNA: ").upper() #upper só para não ter que ficar apertando shift ao digitar
invertida = ""

for c in fita:
  if c == "A":
    invertida = "T" + invertida
  elif c == "C":
    invertida = "G" + invertida
  elif c == "T":
    invertida = "A" + invertida
  elif c == "G":
    invertida = "C" + invertida
  else:
    invertida = c + invertida

print(invertida)