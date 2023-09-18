'''2 - Cremilda Chantilly é uma dentista e precisa de ajuda para o gerenciamento de filas de atendimento. Desenvolva um programa que permita adicionar pacientes na fila e indique a vez do paciente a ser atendido. Adicionar paciente e remover paciente.'''

fila = []

while True:
  print('\n=== Operadores ===\n1*- Digite "1" ou "Adicionar" para adicionar um paciente \n2*- Digite "2" ou "Atender" para atender um paciente \n3*- Digite "3" ou "Checar" para mostrar a fila atual \n4*- Digite "4" ou "Sair" para sair\n')
  escolha = input("Opção: ").upper()
  print()

  # Adicionar a fila
  if escolha == "ADICIONAR" or escolha == "1":
    nome_paciente = input("Digite o nome do paciente a ser adicionado: ")
    fila.append(nome_paciente)

  # Remover da fila
  elif escolha == "ATENDER" or escolha == "2":
    if fila:
      paciente_removido = fila.pop(0)
      print(f"Próximo paciente a ser atendido: {paciente_removido}")
    else:
      print("A fila está vazia.")

  # Checar a fila
  elif escolha == "CHECAR" or escolha == "3":
    if fila:
      print("Fila atual de pacientes:")
      contador = 1
      for paciente in fila:
        print(f"{contador}. {paciente}")
        contador += 1
    else:
        print("A fila está vazia.")

  # Sair
  elif escolha == "SAIR" or escolha == "4":
      break
    
  else:
      print("Opção inválida. Digite novamente.")
