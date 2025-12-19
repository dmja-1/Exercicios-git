soma = 0
q_pares = 0
for x in range(1, 51):
    if x % 2 == 0:
        soma += x
        q_pares += 1
print(soma)
print(q_pares)