'''9) Uma molécula de DNA é composta de duas fitas. Em cada uma temos uma sequência
de nucleotídeos, representados por letras, A (Adenina), C (Citosina), G (Guanina) e T
(Timina). Por exemplo, ACTAGCCATCGA é uma fita de DNA. O RNA é uma molécula
semelhante ao DNA. Porém, tem apenas uma fita e no lugar de T (Timina) encontramos
U (Uracila). A transcrição é um processo que copia uma fita de DNA (ou parte dela) em
uma molécula de RNA. Por exemplo, ACUAGCCAUCGA é a transcrição da fita de DNA
acima. Escreva um algoritmo que leia uma fita de DNA e escreva a transcrição na molécula
de RNA correspondente.'''

fita = input("Digite uma fita de dna: ").upper() #upper só para não ter que ficar apertando shift
rna = ""

for c in fita:
  if c == "T":
    rna += "U"
  else:
    rna += c

print(f"A transcrição da fita é: {rna}")