'''3) Escreva um algoritmo que realize multiplicações consecutivas de dois números reais. Ele deve ser encerrado quando receber uma das entradas igual a 0.'''

print("Multiplicador consecultivo de dois números reais:")
print("# Precione Ctrl+D para sair.")

while True:
  n1 = float(input())
  n2 = float(input())
  
  if n1 == 0 or n2 == 0:
      print("O processamento encerrou porque um dos valores é igual a 0.")
      break
  
  print(n1*n2)
