fim = int(input('\nDigite o último número da sequência: '))
soma_pares = 0
if 1 < fim:
    for x in range(1, fim+1):
        if x % 2 == 0:
            soma_pares += x
else:
    for x in range(1, fim-1, -1):
        if x % 2 == 0:
            soma_pares += x
print(f'\nA soma dos números pares é de: {soma_pares}')
print('\nfim do programa;')