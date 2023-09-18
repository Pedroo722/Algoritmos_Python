'''
Desafio do Beecrowd. Lista 3 Questão 3

'Você está ajudando a desenvolver um sistema de gerenciamento de weblog chamado bloggo. Embora bloggo coloque todo o conteúdo direto no website em HTML, nem todos autores apreciam usar tags HTML em seus textos. Para tornar a vida deles mais fáceis, bloggo oferece uma sintaxe simples chamada atalhos para obter alguns efeitos textuais em HTML. Sua tarefa é, dado um documento escrito com atalhos, traduzi-lo para o HTML apropriado.'

'''

while True:
    try:
      # Entrada do código em sintaxe de webblog
        texto = input()

      # Flags
        italico = 0
        negrito = 0
        fim_de_linha = ''

      # Processamento
        for palavra in range(len(texto)):
            if(texto[palavra] == '_'):
                if(italico == 0):
                    fim_de_linha += '<i>'
                    italico = 1
                else:
                    fim_de_linha += '</i>'
                    italico = 0
           
            elif(texto[palavra] == '*'):
                if(negrito == 0):
                    fim_de_linha += '<b>'
                    negrito = 1
                else:
                    fim_de_linha += '</b>'
                    negrito = 0
                   
            else:
                fim_de_linha += texto[palavra]

      # Saída do código re-escrito em HTML
        print(fim_de_linha)
        
    except EOFError:
        break