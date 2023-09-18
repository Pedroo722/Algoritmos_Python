'''4) Escreva um algoritmo que leia as 4 médias bimestrais para cada um dos 40 alunos de uma
turma. Em seguida, deve se calcular e imprimir a média anual de cada aluno e a média
anual da turma.'''

print("Digite 4 notas para cada um dos 40 aluno: ")

for aluno in range(4):
  
  media = 0
  for prova in range(4):
    prova = float(input())
    media += prova

  resultado = media / 4
  
  print(f"A média do aluno foi {resultado}")
  prova = 0