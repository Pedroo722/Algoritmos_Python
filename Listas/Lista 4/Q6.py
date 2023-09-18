# Escreva um algoritmo que recebe o peso e a altura de uma pessoa, calcule o IMC (peso/altura2) e sua faixa de risco de acordo com a tabela abaixo.

peso = float(input("Digite seu peso em quilogramas: "))
altura = float(input("Digite sua altura em metros: "))

IMC = peso / (altura ** 2)

print("Seu IMC é igual a", IMC)

if IMC < 20:
  print("Seu IMC indica que você está abaixo do peso.")
elif 20 < IMC < 25:
  print("Seu IMC indica que você está na faixa de peso normal.")
elif 25 <= IMC < 30:
  print("Seu IMC indica que você está em excesso de peso.")
elif 30 <= IMC < 35:
  print("Seu IMC indica que você está na faixa de obesidade.")
elif IMC > 35:
  print("Seu IMC indica que você está na  faixa de obesidade mórbida.")