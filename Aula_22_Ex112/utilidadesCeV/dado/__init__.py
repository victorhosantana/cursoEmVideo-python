#Função para o Deafio 112

def entradaMoeda():
    while True:

        resposta = str(input('Informe o valor a ser calculado: R$')).replace(' ','').replace(',', '.')
        if resposta.isnumeric():
            resposta = float(resposta)
            return resposta
        else:
            print(f'\033[31mERRO! A entrada "{resposta}" é inválida! Tente novamente.\033[0m')