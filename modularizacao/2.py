def calculo_media(nota1, nota2, nota3, tipo):
    if tipo.upper() == 'A':
        media = (nota1 + nota2 + nota3) / 3
    elif tipo.upper() == 'P':
        media = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / 10
    elif tipo.upper() == 'H':
        media = 3 / ((1 / nota1) + (1 / nota2) + (1 / nota3))
    return media

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
print("Qual a modalidade desejada?")
tipo = (input("(A) Média Aritmética (P) Média Ponderada (H) Média Harmônica\n"))

media = calculo_media(n1, n2, n3, tipo)

print(f'Média: {media:.2f}')