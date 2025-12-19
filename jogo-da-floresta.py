import random
print('Seja bem-vindo ao Jogo da Floresta!')
vida = 100
energia = 10
tesouro = 0

while vida > 0 and energia >= 0 and tesouro < 3:
    print(f'Vida: {vida}/100 | Energia: {energia}/10 | Tesouros: {tesouro}')
    print('Você anda pela floresta e encontra uma bifurcação')
    entrada = int(input('Você...\n(1) Pega a esquerda\n(2) Pega a direita\n(3) Descansa\n'))

    if entrada == 1:
        print('Você pega a esquerda e acha um urso! Você...')
        escolha_urso = int(input('(1) Luta\n(2) Corre\n'))
        if escolha_urso == 1:
            print('Perde 2 de energia')
            energia -= 2
            x = random.randint(0, 3)
            if x == 3:
                print('Você luta contra o urso e vence! Você acha um tesouro brilhante!')
                print('Ganha 1 tesouro')
                tesouro += 1
            else:
                print('Você luta contra o urso e perde!')
                print('Perde 20 de vida')
                vida -= 20
        else:
            print('Você corre do urso e cai em diversos espinhos!')
            print('Perde 10 de vida e 3 de energia')
            vida -= 10
            energia -= 3

    elif entrada == 2:
        print('Você acha um baú! Você...')
        escolha1 = int(input('(1) Abrir baú\n(2) Deixar o baú\n'))
        if escolha1 == 1:
            print('Perde 1 de energia')
            energia -= 1
            y1 = random.randint(0, 1)
            if y1 == 1:
                print('Você consegue abrir o baú!')
                print('Ganha 1 tesouro')
                tesouro += 1
            else:
                print('Você tenta abrir e não consegue! 2 tentativas restantes. Você...')
                escolha2 = int(input('(1) Abrir baú\n(2) Deixar o baú\n'))
                if escolha2 == 1:
                    y2 = random.randint(0, 1)
                    if y2 == 1:
                        print('Você consegue abrir o baú!')
                        print('Ganha 1 tesouro')
                        tesouro += 1
                    else:
                        print('Você tenta abrir e não consegue! 1 tentativa restante. Você...')
                        escolha3 = int(input('(1) Abrir baú\n(2) Deixar o baú\n'))
                        if escolha3 == 1:
                            y3 = random.randint(0, 1)
                            if y3 == 1:
                                print('Você consegue abrir o baú!')
                                print('Ganha 1 tesouro')
                                tesouro += 1
                            else:
                                print('Você tentou e tentou, mas não conseguiu!')
                                print('Perde 2 de energia pelo estresse')
                                energia -= 2
                        else:
                            print('Você decide deixar o baú de lado')
                else:
                    print('Você decide deixar o baú de lado')
        else:
            print('Você decide deixar o baú de lado')

    elif entrada == 3:
        print('Você decide descansar!')
        descanso = random.randint(0, 4)
        if descanso == 0:
            print('Você tem uma péssima noite de sono!')
            print('Ganha nada e nem perde nada')
        elif descanso == 1:
            print('Você tem uma noite decente!')
            print('Ganha 1 ponto de energia')
            energia += 1
            if energia > 10:
                energia = 10
        elif descanso == 2:
            print('Você tem uma noite muito boa de sono!')
            print('Ganha 3 de energia')
            energia += 3
            if energia > 10:
                energia = 10
        elif descanso == 3:
            print('Você teve uma das melhores noites de sono da sua vida!')
            print('Ganha 4 de energia e 10 de vida')
            energia += 4
            if energia > 10:
                energia = 10
            vida += 10
            if vida > 100:
                vida = 100
        elif descanso == 4:
            print('Você sonha com o paraíso!')
            print('Ganha 5 de energia, 20 de vida e 1 tesouro')
            energia += 5
            if energia > 10:
                energia = 10
            vida += 20
            if vida > 100:
                vida = 100
            tesouro += 1

    else:
        print('Você se perde um dia inteiro e se fere!')
        print('Perde 15 de vida e 5 de energia')
        vida -= 15
        energia -= 5
    print('=======================================================')

if vida <= 0:
    print('Você morreu!')
    print('Game over!')
if energia < 0:
    print('Você morre de exaustão!')
    print('Game over!')
if tesouro == 3:
    print('Você venceu o jogo!')
    print('Obrigado por jogar!')