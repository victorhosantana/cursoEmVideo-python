#Cria uma função que pode adaptar o tamanho dos traços na impressão de uma String
def escreva(msg):
    linhas = len(msg) + 4
    print('~' * linhas)
    print(' ', msg)
    print('~' * linhas)


escreva('Teste')
escreva('Textinho bem maior')
escreva('Textinho muito, muito, muito mesmo, maior')
escreva('Um bocado de texto que só serve pra encher linguiça e aumentar o espaço da String')
