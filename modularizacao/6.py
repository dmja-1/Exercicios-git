''' Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna
    essa idade expressa em dias '''

def calcularDias(anos, meses, dias):

    anos_em_dias = anos * 365

    meses_em_dias = meses * 30

    resultado = anos_em_dias + meses_em_dias + dias

    return resultado

anos = int(input('Digite a idade em anos: '))
meses = int(input('Digite os meses: '))
dias = int(input('Digite os dias: '))

resultado = calcularDias(anos, meses, dias)

print(f'A idade em dias é de {resultado} dias!')