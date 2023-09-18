'''4) Escreva um algoritmo que leia as 4 médias bimestrais para cada um dos 40 alunos de uma turma. Em seguida, deve se calcular e imprimir a média anual de cada aluno e a média anual da turma. Mantenha as médias todas em uma lista, estrutura que deve ser criada ao longo da entrada. Crie métodos, a sua escolha, para usar durante o processamento dos dados.'''

def media_anual(notas_bimestrais):
    return sum(notas_bimestrais) / len(notas_bimestrais)

turma = []

for aluno in range(40):
    print(f"Aluno {aluno + 1}:")
    notas_bimestrais = []
  
    for bimestre in range(4):
        nota = float(input(f"Nota do {bimestre + 1}* bimestre: "))
        notas_bimestrais.append(nota)
      
    media_aluno = media_anual(notas_bimestrais)
    turma.append(media_aluno)
    print(f"Média anual do aluno {aluno + 1}: {media_aluno:.2f}\n")

media_turma = media_anual(turma)
print(f"Média anual da turma: {media_turma:.2f}")
