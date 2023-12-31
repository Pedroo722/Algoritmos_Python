'''
Lista 3 Questão 1

Desafio do Beecrowd, retirado da Maratona de Programação SBC Brasil.


Machado gosta muito de escrever. Já escreveu muitos contos, resenhas, relatos de viagens que fez, além de um pequeno romance. Agora Machado quer participar de um concurso de contos, que tem regras muito rígidas sobre o formato de submissão do conto. As regras do concurso especificam o número máximo de caracteres por linha, o número máximo de linhas por página, além de limitar o número total de páginas. Adicionalmente, cada palavra deve ser escrita integralmente em uma linha (ou seja, a palavra não pode ser separada silabicamente em duas linhas). Machado quer escrever um conto com o maior número de palavras possível, dentro das regras do concurso, e precisa de sua ajuda. Dados o número máximo de caracteres por linha, o número máximo de linhas por página, e as palavras do conto que Machado está escrevendo, ele quer saber o número mínimo de páginas que seu conto utilizaria seguindo as regras do concurso.

Crie um programa para suprir as necessidades de Machado.
'''

from math import ceil


while True:
    try:
      # Entrada do número de palavras, linhas e caractéres
        N, L, C = [int(x) for x in input().split()]
      
      # Entrada do texto de Machado
        texto = input().split()

      # Processamento
        aux = texto[0]
        total_linhas = 1

      
        for i in range(1, len(texto)):
            if C >= len(aux + ' ' + texto[i]):
                aux += ' ' + texto[i]
            else:
                total_linhas += 1
                aux = texto[i]

      # Saída
        print(ceil(total_linhas / L))

    except EOFError:
        break