import math

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None  # sem raízes reais

    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    return x1, x2  # retorna as duas formas

a = float(input())
b = float(input())
c = float(input())

resultado = bhaskara(a, b, c)

if resultado:
    x1, x2 = resultado
    print("x1 =", x1)
    print("x2 =", x2)
else:
    print("Não há raízes reais")

''' dá para acessar os diferentes return colocando numa variavel e então acessando ela com outras variaveis separadas por virgula
    recebendo o valor do return'''