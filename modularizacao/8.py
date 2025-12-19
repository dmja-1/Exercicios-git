def verificarCategoria(idade):
    if idade < 5:
        return 'Não qualificado para nenhuma categoria'
    elif 5 <= idade <= 7:
        return 'Infantil A'
    elif 8 <= idade <= 10:
        return 'Infantil B'
    elif 11 <= idade <= 13:
        return 'Juvenil A'
    elif 14 <= idade <= 17:
        return 'Juvenil B'
    else:
        return 'Adulto'

idade = int(input('Digite sua idade: '))
print(verificarCategoria(idade))

''' Precisamos botar apenas "return" ao invés de print(), pois se botarmos print, ele entenderá que o return é vazio, então ele vai
    imprimir de acordo com a categoria, só que também imprimirá na linha abaixo "none" '''