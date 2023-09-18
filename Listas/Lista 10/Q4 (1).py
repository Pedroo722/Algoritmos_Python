'''4) Escreva um algoritmo que leia duas strings e encontre a maior substring comum entre elas. Como saida deve imprimir o tamanho desta maior substring.'''

frase1 = input("Digite a primeira frase: ")
frase2 = input("Digite a segunda frase: ")

tamanho_substring = 0

for i in range(len(frase1)):
  for j in range(len(frase2)):
    tamanho_substring_atual = 0
  
  # gostaria de ter deixado esse While mais bonito/legivel, mas não faco ideia de como conseguir simplificar
    while (i + tamanho_substring_atual < len(frase1) and \
           j + tamanho_substring_atual < len(frase2) and \
           frase1[i + tamanho_substring_atual] == frase2[j + tamanho_substring_atual]):
      tamanho_substring_atual += 1

    if tamanho_substring_atual > tamanho_substring:
      tamanho_substring = tamanho_substring_atual

if tamanho_substring == 0:
    print("Não houve substrings em comum.")
else:
    print(f"O tamanho da maior substring comum entre elas é: {tamanho_substring}")
