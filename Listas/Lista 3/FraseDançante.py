'''
Desafio do Beecrowd. Lista 3 Questão 2

Uma sentença é chamada de dançante se sua primeira letra for maiúscula e cada letra subsequente for o oposto da letra anterior. Espaços devem ser ignorados ao determinar o case (minúsculo/maiúsculo) de uma letra. Por exemplo, "A b Cd" é uma sentença dançante porque a primeira letra ('A') é maiúscula, a próxima letra ('b') é minúscula, a próxima letra ('C') é maiúscula, e a próxima letra ('d') é minúscula.

Crie um programa que transforme a sentença de entrada em uma sentença dançante, trocando as letras para minúscula ou maiúscula onde for necessário. Todos os espaços da sentença original deverão ser preservados, ou seja, " sentence " deverá ser convertido para " SeNtEnCe ".
'''



while True:
    try:
      # Entrada do texto
        linha_nova = ""
        linha = input()

      # Flag
        maiuscula = True

      # Processamento
        for letra in linha:
            if letra == ' ':
                linha_nova += ' '
            elif maiuscula:
                linha_nova += letra.upper()
                maiuscula = False
            else:
                linha_nova += letra.lower()
                maiuscula = True

      # Saída
        print(linha_nova)
    except EOFError:
        break
