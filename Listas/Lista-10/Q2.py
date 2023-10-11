'''2) Escreva um algoritmo que realize somas consecutivas de dois números reais. Ele deve ser encerrado quando receber duas entradas iguais a 0. Utilize o comando break para encerrar a execução.'''


print("Somador consecultivo de dois números reais:")
print("# Precione Ctrl+D para sair.")

while True:
  n1 = float(input())
  n2 = float(input())
  
  if n1 == 0 and n2 == 0:
    print("O processamento encerrou porque os dois valores são iguais a 0.")
    break
  
  print(n1+n2)
