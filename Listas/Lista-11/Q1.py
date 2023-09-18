'''1) Escreva uma algoritmo que repetitivamente leia dois números, limite inferior e limite superior, e em seguida faça uma chamada a uma função que receba estes limites e imprima o intervalo delimitado pelos limites. O algoritmo deve ser interrompido quando as entradas forem 0 (zero).'''

def intervalo(a,b):
  print(f"O intervalo de {a} e {b} é:")
  if a > b:
    for x in range(a,b-1,-1):
      print(x)
  if a < b:
    for x in range(a,b+1):
      print(x)

while True:
  n1 = int(input("Digite um número: "))
  n2 = int(input("Digite um outro número: "))
  if n1 == 0 and n2 == 0:
    print("O processo foi interrompido porque as duas entradas são 0.")
    break
  intervalo(n1,n2)