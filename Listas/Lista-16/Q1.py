'''1 - Cicinho Cabeça é mecânico e anda meio broco. Precisa de sua ajuda. Desenvolva um programa que receba os nomes das peças que ele está removendo,  na ordem e depois vá indicando uma a uma, na ordem inversa da adição. Operações adicionar peça e remover peça.'''

from collections import deque

pecas = []

while True:
  print('\n=== Operadores ===\n1*- Digite "1" ou "Adicionar" para adicionar uma peça \n2*- Digite "2" ou "Remover" para remover a última peça \n3*- Digite "3" ou "Checar" para ver as peças atuais \n4*- Digite "4" ou "Sair" para sair\n')
  escolha = input("Opção: ").upper()
  print()

  # Adicionar a pilha
  if escolha == 'ADICIONAR' or escolha == '1':
    add = input("Digite o nome da peça a ser adicionada: ")
    pecas.append(add)

  # Remover da pilha
  elif escolha == 'REMOVER' or escolha == '2':
    if pecas:
      print("Foi removido:")
      print(pecas.pop())
    else:
      print("Não há peças para remover.")

  # Checar a pilha
  elif escolha == 'CHECAR' or escolha == '3':
    print("Peças atuais:")
    if len(pecas) > 0:
      for peca in pecas:
        print(peca)
    else:
      print("Não há peças.")

  # Sair
  elif escolha == 'SAIR' or escolha == '4':
    break
      
  else:
    print("Opção inválida. Digite novamente.")

print("Peças restantes:")
if len(pecas) > 0:
  for peca in pecas:
    print(peca)
else:
  print("Não houve peças restantes.")
