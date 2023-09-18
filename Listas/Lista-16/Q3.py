'''3 - Desenvolva uma v2 para o programa das filas. Desta vez ele deve manter 2 filas, uma par atendimentos regulares e outra para prioridades. No atendimento começar pela prioridade, se houver, e em seguida ir alternando, ou seja, um prioridade, um regular, outro prioridade e outro regular, até o final das filas.'''

fila_prioridade = []
fila_regular = []

while True:
  print('\n=== Operadores ===\n1*- Digite "1" ou "Prioridade" para adicionar um paciente na fila com prioridade\n2*- Digite "2" ou "Regular" para adicionar um paciente na fila regular \n3*- Digite "3" ou "Atender" para atender o próximo paciente \n4*- Digite "4" ou "Checar" para mostrar as filas \n5*- Digite "5" ou "Sair" para sair\n')
  escolha = input("Opção: ").upper()
  print()

  # Adicionar a fila PRIORIDADE
  if escolha == "PRIORIDADE" or escolha == "1":
    nome_paciente1 = input("Digite o nome do paciente com prioridade: ")
    fila_prioridade.append(nome_paciente1)

  # Adicionar a fila REGULAR
  elif escolha == "REGULAR" or escolha == "2":
    nome_paciente2 = input("Digite o nome do paciente regular: ")
    fila_regular.append(nome_paciente2)

  # Remover da fila
  elif escolha == "ATENDER" or escolha == "3":
    if fila_prioridade:
      paciente_removido = fila_prioridade.pop(0)
      print(f"Próximo paciente a ser atendido (Prioridade): {paciente_removido}")
    elif fila_regular:
      paciente_removido = fila_regular.pop(0)
      print(f"Próximo paciente a ser atendido (Regular): {paciente_removido}")
    else:
      print("Ambas as filas estão vazias.")

  # Checar a fila
  elif escolha == "CHECAR" or escolha == "4":
    if fila_prioridade:
      print("Fila de prioridade:")
      contador = 1
      for paciente in fila_prioridade:
        print(f"{contador}. {paciente}")
        contador += 1
        
    if fila_regular:
      print("\nFila regular:")
      contador = 1
      for paciente in fila_regular:
        print(f"{contador}. {paciente}")
        contador += 1
        
    if fila_prioridade == [] and fila_regular == []:
      print("Ambas as filas estão vazias.")

  # Sair
  elif escolha == "SAIR" or escolha == "5":
      break
    
  else:
      print("Opção inválida. Digite novamente.")