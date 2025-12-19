''' Faça uma função que recebe um valor inteiro e verifica se o valor é positivo ou
negativo. A função deve retornar um valor booleano. '''

def verificarNumero(num):

    flag = True

    if num < 0:
        flag = False

    return flag

num = int(input('Digite seu número para verificação: '))
print('FLAGS: True = Positivo, False = Negativo\n')
print(f'NUMERO_STATUS: {verificarNumero(num)}')