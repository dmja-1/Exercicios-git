''' Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A
    função deve retornar um valor booleano '''

def verificarNumero(num):

    flag = True

    if num % 2 != 0:
        flag = False

    return flag

num = int(input('Digite seu número para verificação: '))
print('FLAGS: True = Par, False = Ímpar\n')
print(f'NUMERO_STATUS: {verificarNumero(num)}')