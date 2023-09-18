'''3) Escreva um algoritmo que leia uma matriz de dimensão escolhida pelo usuário. Em seguida, deve calcular e imprimir o determinante.'''

linhas_matriz = int(input("Digite o número de linhas da matriz: "))
colunas_matriz = int(input("Digite o número de colunas da matriz: "))

if linhas_matriz != colunas_matriz:
  print("Não é possível calcular o determinante. Por definição a matriz deve ser quadrada.")
else:
  dimensao = linhas_matriz
  print("\nDigite os elementos da matriz separados por espaço:")
  print("\n== Exemplo: ==\n* (5 5)\n* (2 3)")
  print("================\n")
  matriz = [list(map(int, input("Digite uma linha: " ).split())) for i in range(linhas_matriz)]

  if dimensao == 1:
    determinante = matriz[0][0] # Lembrete pessoal: o único elemento da matriz ainda é uma lista dentro de uma lista, por isso precisa de [0][0]
    
  elif dimensao == 2:
    determinante = (matriz[0][0] * matriz[1][1]) - (matriz[0][1] * matriz[1][0])
    
  elif dimensao == 3:
    determinante = 0
    for i in range(3):
        cofator = matriz[0][i] * (matriz[1][(i+1)%3] * matriz[2][(i+2)%3] - matriz[1][(i+2)%3] * matriz[2][(i+1)%3])
        determinante += cofator
      
  elif dimensao == 4:
  # Não acho que o resultado esteja 100% certo, mas tentei
    determinante = 0
    for i in range(4):
        cofator = matriz[0][i] * (matriz[1][(i+1)%4] * matriz[2][(i+2)%4] * matriz[2][(i+3)%4] - matriz[1][(i+2)%4] * matriz[2][(i+1)%4] * matriz[3][(i+3)%4])
        determinante += cofator
      
  elif dimensao > 4:
  # Não faço ideia de como fazer para calcular com 5 ou mais dimensões
    print("Desculpe. A dimensão da matriz excede o limite previsto.")

  print(f"O determinante da matriz é: {determinante}")