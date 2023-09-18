'''7) Você foi contratado pela Federação Paraibana de Futebol e sua primeira tarefa é desenvolver um programa que receba como entrada uma sequência de resultados de partidas de um determinado time e gere como saída a pontuação do time de acordo com os resultados. O resultado pode ser V (Vitória), E (Empate) ou D (Derrota). Uma vitória vale 3 pontos, empate 1 e derrota 0. VVEEEDVDEV é um exemplo de sequência. A respectiva pontuação
do time para esta sequência é 16.'''

sequencia = input("Digite uma sequência de resultados de partidas. \nNa forma de V (Vitória), E (Empate) ou D (Derrota) \n(Exemplo: VVDEV = 10) \nResultado: ").upper() #upper só para não ter que ficar apertando shift

resultado = 0

for c in sequencia:
  if c == "V":
    resultado += 3
  elif c == "E":
    resultado += 1
  elif c == "D":
    resultado += 0

print(f"O resultado final foi: {resultado}")