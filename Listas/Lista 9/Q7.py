'''7) Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos. Exemplo: 120 é triangular, pois 4 × 5 × 6 = 120. Dado um inteiro não negativo n, verificar se n é triangular.'''


numero = int(input("Digite um número inteiro positivo: "))

if numero >= 0:
    
  i = 0
  
  while i * (i + 1) * (i + 2) < numero:
    i += 1
    
  if i * (i + 1) * (i + 2) == numero:
    print(f"{numero} é um número triangular.")
  else:    
    print(f"{numero} não é um número triangular.")


else:
  print("O número não é um inteiro positivo.") 