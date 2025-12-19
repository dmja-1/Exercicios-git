''' Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito
quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3,
que são seus divisores). A função deve retornar um valor booleano. '''

def calcularPerfeito(num):
    flag = False
    variavel = 0
    for x in range(1, num):
        if num % x == 0:
            variavel += x
    if variavel == num:
        flag = True
    return flag
    
num = int(input("Digite o número para verificar se é perfeito: "))
perfeito = calcularPerfeito(num)

print(f'PERFEITO_STATUS: {perfeito}')

