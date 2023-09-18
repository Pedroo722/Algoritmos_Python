#Escreva um algoritmo que receba as três médias de um aluno, calcule a média semestral, e informe se o aluno passou de ano ou reprovou

print("Digite as três médias do aluno:")

media1 = int(input())
media2 = int(input())
media3 = int(input())

mediafinal = (media1 + media2 + media3) / 3

if mediafinal >= 7:
  print("O aluno passou de ano. Sua média total foi: ", mediafinal)
elif 7 > mediafinal >= 4:
  print("O aluno deverá fazer a prova final. Sua média total foi: ", mediafinal)
elif mediafinal < 4:
  print("O aluno reprovou de ano. Sua média total foi: ", mediafinal)