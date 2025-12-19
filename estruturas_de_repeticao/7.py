soma_impar = 0
soma = 0
for x in range(20, 51):
    if x % 2 != 0:
        soma_impar += x
    soma += x
print(soma_impar)
print(soma)