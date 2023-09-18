'''1) Escreva um algoritmo que leia 2 matrizes, calcule e escreva o produto delas. O algoritmo deve permitir matrizes de diversas dimensões e deve validar se é possível calcular.'''

linhas_matriz1 = int(input("Digite o número de linhas da primeira matriz: "))
colunas_matriz1 = int(input("Digite o número de colunas da primeira matriz: "))
linhas_matriz2 = int(input("Digite o número de linhas da segunda matriz: "))
colunas_matriz2 = int(input("Digite o número de colunas da segunda matriz: "))

if colunas_matriz1 != linhas_matriz2:
  print("As matrizes não podem ser multiplicadas.")
else:
# Primeira Matriz
  
  print("\nDigite os elementos da primeira matriz separados por espaço:")
  print("\n== Exemplo: ==\n* (5 5)\n* (2 3)")
  print("================\n")
  
  matriz1 = [list(map(int, input("Digite uma linha: " ).split())) for i in range(linhas_matriz1)]

# Segunda Matriz
  
  print("\nDigite os elementos da segunda matriz separados por espaço:")
  print("\n== Exemplo: ==\n* (2 6)\n* (4 6)")
  print("================\n")
  
  matriz2 = [list(map(int, input().split())) for i in range(linhas_matriz2)]

# Cálculo
  resultado = []
  
  for i in range(linhas_matriz1):
    linha_resultado = []
    for j in range(colunas_matriz2):
      soma = 0
      for k in range(colunas_matriz1):
          soma += matriz1[i][k] * matriz2[k][j]
      linha_resultado.append(soma)
    resultado.append(linha_resultado)

  print("\nO produto das matrizes é:")
  for linha in resultado:
      print(linha)