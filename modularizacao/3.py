def primo(num):
    if num < 2:
        return False
    flag = True

    for x in range(2, num):
        if num % x == 0:
            flag = False
            break
    return flag

num = int(input("Digite um número para verificarmos se é primo: "))
print(f'PRIMO_STATUS: {primo(num)}')

''' defino que automaticamente qualquer numero menor de 2 NÃO É primo, depois, assumo que qualquer numero é primo, e crio um caso
    que caso algum numero na estrutura de repetição seja divisivel pelo numero informado e dê resultado 0, ele assume então que o
    numero informado não é primo, e é necessario o break para que a estrutura de repetição cancele, pois senão irá considerar somente
    o ultimo numero e continuará '''