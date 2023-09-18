# Escreva um algoritmo que recebe três inteiros e escreva o maior deles como saída.

print("Digite três números:")
Num1 = int(input())
Num2 = int(input())
Num3 = int(input())

if (Num1 > Num2) and (Num1 > Num3):
  print(f"O maior número é: {Num1}")
elif (Num2 > Num1) and (Num2 > Num3):
  print(f"O maior número é {Num2}")
elif (Num3 > Num1) and (Num3 > Num2):
  print(f"O maior número é {Num3}")
