def volume_esfera(raio):
    volume = (4 * 3.14 * (raio ** 3)) / 3
    return volume

raio = int(input('Digite o valor do raio da esfera: '))

print(f'O volume é de {volume_esfera(raio):.2f}')