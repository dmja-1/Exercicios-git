try:
    fim = int(input('\nDigite o número final da sequência: '))
    soma = 0
    produtos = 1
    if 100 < fim:
        for x in range(100, fim+1):
            if x % 2 == 0:
                soma += x
            else:
                produtos *= x
    else:
        for x in range(100, fim-1, -1):
            if x % 2 == 0:
                soma += x
            else:
                produtos *= x
    print('\n=== RESUMO ===')
    print(f'\nSOMA DOS NÚMEROS PARES: {soma} --- PRODUTO DOS NÚMEROS ÍMPARES: {produtos}')
    print('\nfim do programa;')
except ValueError:
    print('\nO valor digitado precisa ser um número inteiro!')
    print('\nfim do programa;')