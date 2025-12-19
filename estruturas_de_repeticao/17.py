'''Faça um programa que mostra os valores a partir de um intervalo informado pelo
usuário. Mostre quantos valores pares estão no intervalo e a soma deles, bem como quantos
ímpares e a media desses valores; Atenção, teste se o usuário digitou valores válidos, por ex: 2 e 6
irá mostrar 2, 3, 4, 5, 6; Entretanto, se o usuário digitar 6 e 2, não será possível mostrar valores.'''

entrada = input('\nEscreva o início e o fim do conjunto: ').split()
comeco = int(entrada[0])
fim = int(entrada[1])
q_pares = 0
soma_pares = 0
q_impares = 0
soma_impares = 0

if fim <= comeco:
    print('Erro!')
else:
    for x in range(comeco, fim+1):
        if x % 2 == 0:
            q_pares += 1
            soma_pares += x
        else:
            q_impares += 1
            soma_impares += x
    media_impares = soma_impares / q_impares
    print('\n=== RESUMO ===\n')
    print(f'QUANTIDADE DE NÚMEROS PARES: {q_pares} --- SOMA DOS NÚMEROS PARES: {soma_pares}')
    print(f'QUANTIDADE DE NÚMEROS ÍMPARES: {q_impares} --- MÉDIA DOS NÚMEROS ÍMPARES: {media_impares:.1f}')
    print('\nfim do programa;')