entrada = input('Escreva o início e o fim do conjunto: ').split()
comeco = int(entrada[0])
fim = int(entrada[1])
soma = 0

if comeco > fim:
    for x in range(comeco, fim-1, -1):
        soma += x
    print(soma)
else:
    for x in range(comeco, fim+1):
        soma += x
    print(soma)