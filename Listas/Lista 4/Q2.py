# Escreva um algoritmo que calcule as raízes de uma equação do 2* grau, na forma ax2+bx+c.

import math

a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c
print("Delta é igual a: ", delta)

for x in str(delta):
  if delta < 0:
    print("A equação não possui raizes reais.")
    break
  elif delta == 0:
    x = -b / (2*a)
    print("A equação possui apenas uma única raiz: ", x)
    break
  elif delta > 0:
    Raiz1 = (-b + math.sqrt(delta)) / (2*a)
    Raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print("A equação possui duas raizes reais.", "\nPrimeira raiz: ", Raiz1, "\nSegunda raiz: ", Raiz2)
    break