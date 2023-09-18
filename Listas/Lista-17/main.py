'''1) Implemente um sistema de informação que mantenha informações a respeito de alunos. Deve manter matrícula, nome, data de nascimento e ano de ingresso. O sistema deve listar os cadastrados, permitir inserção, remoção e alteração. Use dicionário e classe.'''

class Aluno:
  def __init__(self, matricula, nome, nascimento, ingresso):
    self.matricula = matricula
    self.nome = nome
    self.nascimento = nascimento
    self.ingresso = ingresso

# Adicionar
def adicionar_aluno(alunos):
  matricula = input("\nMatrícula: ")
  if matricula in alunos:
    print("\nEssa matrícula já está cadastrada.")
  else:
    nome = input("Nome: ")
    nascimento = input("Data de Nascimento: ")
    ingresso = input("Ano de Ingresso: ")
    aluno = Aluno(matricula, nome, nascimento, ingresso)
    alunos[matricula] = aluno
    print("\nAluno cadastrado com sucesso.")

# Checar
def checar_alunos(alunos):
  if alunos == {}:
    print("\nNenhum aluno cadastrado.")
  else:
    print("\n==Alunos Cadastrados==")
    for matricula, aluno in alunos.items():
      print(f"Matrícula: {matricula}")
      print(f"* Nome: {aluno.nome}")
      print(f"* Data de Nascimento: {aluno.nascimento}")
      print(f"* Ano de Ingresso: {aluno.ingresso}")
      print()

# Editar
def alterar_aluno(alunos, matriculado):
  if matriculado in alunos:
    aluno = alunos[matriculado]
    print()
    print(f"Matrícula: {aluno.matricula}")
    print(f"Nome atual: {aluno.nome}")
    novo_nome = input("Novo nome: ")
    print()
    print(f"Data de Nascimento atual: {aluno.nascimento}")
    novo_nascimento = input("Nova data de nascimento: ")
    print()
    print(f"Ano de Ingresso atual: {aluno.ingresso}")
    novo_ingresso = input("Novo ano de ingresso: ")
    
    aluno.nome = novo_nome
    aluno.nascimento = novo_nascimento
    aluno.ingresso = novo_ingresso
    print("\nOs dados do aluno foram alterados com sucesso.")
  else:
    print("\nDesculpe essa matrícula não existe.")
  
# Remover
def remover_aluno(alunos, matriculado):
  if matriculado in alunos:
    del alunos[matriculado]
    print("Aluno removido com sucesso.")
  else:
    print("\nDesculpe, isso não é uma matrícula válida.")

####################
alunos = {}

while True:
  print("\n=== Sistema de Cadastro Escolar ===")
  print("Oque deseja fazer?\n1- Adicionar um novo aluno.\n2- Checar os dados dos alunos atuais.\n3- Alterar os dados de um aluno cadastrado.\n4- Remover um aluno.\n5- Sair\n")
  opcao = input("Opção: ").upper()

  ## opção 1 | adicionar
  if opcao == "1" or opcao == "ADICIONAR":
    adicionar_aluno(alunos)

  ## opção 2 | checar
  elif opcao == "2" or opcao == "CHECAR":
    checar_alunos(alunos)

  ## opção 3 | editar
  elif opcao == "3" or opcao == "ALTERAR":
    if alunos == {}:
      print("\nNenhum aluno cadastrado.")
    else:
      matriculado = input("\nDigite a matricula do aluno a ser alterado: ")
      alterar_aluno(alunos, matriculado)
      
  ## opção 4 | remover
  elif opcao == "4" or opcao == "REMOVER":
    if alunos == {}:
      print("\nNenhum aluno cadastrado.")
    else:
      matriculado = input("\nDigite a matricula do aluno a ser removido: ")
      remover_aluno(alunos, matriculado)
      
  ## opção 5 | sair
  elif opcao == "5" or opcao == "SAIR":
    break
    
  ## opção erro
  else:
    print("\nIsso não é uma opção válida. Digite novamente")