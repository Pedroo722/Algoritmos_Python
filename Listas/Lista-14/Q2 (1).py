'''2) Escreva um algoritmo que leia um inteiro n e uma matriz de dimensão escolhida pelo usuário. Em seguida, deve calcular e escrever o resultado do produto escalar.'''

linhas_matriz = int(input("Digite o número de linhas matriz: "))
colunas_matriz = int(input("Digite o número de colunas matriz: "))

print("\nDigite os elementos da matriz separados por espaço:")
print("\n== Exemplo: ==\n* (5 5)\n* (2 3)")
print("================\n")
matriz = [list(map(int, input("Digite uma linha: " ).split())) for i in range(linhas_matriz)]

escalar = int(input("\nDigite um escalar: "))

resultado = []

print("\nResultado do produto escalar:")
for linha in matriz:
    for elemento in linha:
      resultado = elemento * escalar
      print(resultado, end=" ")
    print()