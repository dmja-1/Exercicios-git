entrada = input('Escreva o início e o fim do conjunto: ').split()
comeco = int(entrada[0])
fim = int(entrada[1])
soma = 0
x = comeco

if comeco > fim:
    while x >= fim:
        soma += x
        x -= 1
else:
    while x <= fim:
        soma += x
        x += 1

print(f"A soma foi de {soma}")