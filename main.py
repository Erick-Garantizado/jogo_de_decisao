from random import randint, choice
from time import sleep
from sys import exit

def d6():
    x = randint(1, 6)
    return x

def d10():
    x = randint(1, 10)
    return x

def d20():
    '''
    os dados de 20 lados diz se o personagem obtem exito ou nao em sua escolha
    '''
    x = randint(1, 20)
    return x

def cabecalho(txt):
    print(linha())
    print(txt.center(75))
    print(linha())

def linha(tam=75):
    return '-' * tam

def linha2(tam=25):
    return '=x=' * tam

def linha3(tam=25):
    return print('¨' * tam)

def pts(x):
    for c in range(0, x):
        sleep(1)
        print('.', end=' ')

def seguir():
    print(linha())
    input('->')
    print(linha())

def batalha():
    print(linha2())
    print('{:>30}'.format('B'), end='')
    sleep(0.5)
    print(' A', end='')
    sleep(0.5)
    print(' T', end='')
    sleep(0.5)
    print(' A', end='')
    sleep(0.5)
    print(' L', end='')
    sleep(0.5)
    print(' H', end='')
    sleep(0.5)
    print(' A')
    sleep(0.5)
    print(linha2())

def continua():
    print(linha2())
    print('{:>30}'.format('C'), end='')
    sleep(0.5)
    print(' O', end='')
    sleep(0.5)
    print(' N', end='')
    sleep(0.5)
    print(' T', end='')
    sleep(0.5)
    print(' I', end='')
    sleep(0.5)
    print(' N', end='')
    sleep(0.5)
    print(' U', end='')
    sleep(0.5)
    print(' A', end='')
    sleep(0.5)
    pts(3)
    print()
    print(linha2())




prota_atrb = {'vida': 10,
             'atk': 4,
             'defe': 15,
             'comida': 2,
             'XP': 0,
             'lvl': 1}

guerreira = {'vida':10,
             'atk': 4,
             'defe':15}

urso = {'vida': 15,
        'atk': 5,
        'defe': 13}

cabecalho('JOGO DA DECISAO')

s = str(input('Qual será o sexo do personagem? M(masculino) F(feminino):\n')).strip().lower()[0]

if s == 'm':
    sexo = ['o', 'ele', 'um']
else:
    sexo = ['a', 'ela', 'uma']

prota = str(input('Qual será o nome do seu Personagem?\n')).strip().capitalize()

print('Enredo:')
print(f'O reino LEMSA foi atacado, o rei RUJE foi assassinado e você, \n{prota}, filh{sexo[0]} do rei, busca vingança.')
print(linha())
print(f'{prota} lotad{sexo[0]} de fúria em seu coração, sem consultar ninguém,\n'
      f'dois dias depois da morte de seu pai, sai bem cedo\n'
      f'para a sua jornada que é ir para o reino vizinho matar o rei Asa.\n'
      f'Pensando {prota} que Asa era o autor do ataque.')
print(linha())
print(f'Equipad{sexo[0]} com sua espada longa, roupa de batalha e 2 pedaços de carne,\n{prota} segue com seu objetivo.')
pts(3)
print(f'\nDurante a caminhada ele encontra uma guerreira nomade que {sexo[0]} ameassa.')
print(linha())
seguir()
print(linha2())
print('O QUE VOCÊ FAZ?')
sleep(0.5)

decisao1 = int(input('[1]Atacar\n'
                     '[2]conversar\n'))
sleep(1)
print(linha())
derrota = False
if decisao1 == 1:
    batalha()
    print(f'                Vida:{prota_atrb["vida"]:<20}  Guerreira:{guerreira["vida"]}')
    linha3(tam=75)

    while True:
#player time
        sleep(0.5)
        print('Sua vez')
        sleep(1)
        ação = int(input('[1] Espada\n[2] Comer\n'))
        if ação == 2:   #logica para prota restaurar vida
            if prota_atrb['vida'] >= 10:
                prota_atrb['vida'] = 10
                print('Sua vida esta cheia, nao precisa comer!')
            elif prota_atrb['comida'] > 0 and -1 < prota_atrb['vida'] < 10:
                prota_atrb['comida'] -= 1
                prota_atrb['vida'] += 3
                print(f'Você ganhou +3 de vida')
                print(f'Qtd. de comida: {prota_atrb["comida"]}')
                if prota_atrb['vida'] > 10:
                    prota_atrb['vida'] = 10
            elif prota_atrb['comida'] < 0:
                print('Você não tem mais comida!')
        else:
            print('Rolando d20')
            dado20 = d20()
            sleep(1)
            tentativa = dado20 + prota_atrb['atk']
            pts(3)

            #critico ou nao
            critical = False
            if dado20 == 20:
                critical = True
                print(f'd20: {dado20} -- CRITICALL !!!')
            else:
                print(f'd20: {dado20}')
            sleep(2)
            print(f'Tentativa: {tentativa}')
            sleep(3)

            #acertou ou nao
            if tentativa >= guerreira['defe']:
                print(linha())
                print('Você acertou! Rolando d10')
                pts(2)
                dado10 = d10()
                print(f'{dado10} de dano')
                guerreira['vida'] -= dado10
                if critical:
                    print('Rolando d10 novamente')
                    pts(2)
                    dado10 = d10()
                    print(f'{dado10} de dano')
                    guerreira['vida'] -= dado10
                print(linha())
            else:
                erros = 'Adversario desviou', 'Você errou!'
                print(choice(erros))
                print(linha())

            if guerreira['vida'] <= 0:
                guerreira['vida'] = 0
                print(f'                Vida:{prota_atrb["vida"]:<20}  Guerreira:{guerreira["vida"]}')
                linha3(tam=75)
                break
        sleep(2)
        print(f'                Vida:{prota_atrb["vida"]:<20}  Guerreira:{guerreira["vida"]}')
        linha3(tam=75)

#enemy time
        sleep(0.5)
        print('Vez do adversário')
        sleep(1)
        print('Rolando d20')
        dado20 = d20()
        sleep(1)
        tentativa = dado20 + guerreira['atk']
        pts(3)

        #critico ou nao
        critical = False
        if dado20 == 20:
            critical = True
            print(f'd20: {dado20} -- CRITICALL !!!')
        else:
            print(f'd20: {dado20}')
        sleep(2)
        print(f'Tentativa: {tentativa}')
        sleep(3)

        #acertou ou nao
        if tentativa >= prota_atrb['defe']:
            print('Adversario acertou! Rolando d10')
            pts(2)
            dado10 = d10()
            print(f'{dado10} de dano')
            prota_atrb["vida"] -= dado10
            if critical:
                print('rolando d10 novamente')
                pts(2)
                dado10 = d10()
                print(f'{dado10} de dano')
                prota_atrb["vida"] -= dado10
            print(linha())
        else:
            erros = 'Você desviou', 'Adversario errou!'
            print(choice(erros))
            print(linha())

        if prota_atrb['vida'] <= 0:
            prota_atrb['vida'] = 0
            print(f'                Vida:{prota_atrb["vida"]:<20}  Guerreira:{guerreira["vida"]}')
            linha3(tam=75)
            break
        sleep(2)
        print(f'                Vida:{prota_atrb["vida"]:<20}  Guerreira:{guerreira["vida"]}')
        linha3(tam=75)

    if guerreira['vida'] <= 0:
        cabecalho('VITORIA')
        input('Press enter to finish')
    else:
        cabecalho('DERROTA')
        derrota = True
        print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
        input('Press enter to finish')
        exit()
else:
    print('Você tenta convencê-la de que não faz sentido vocês lutarem, já que o seu\nobjetivo não é lutar contra ela.')
    linha3()
    seguir()
    linha3()

    print('Ayllah:\n'
          '     - Você tem razão, eu também tenho a minha jornada a seguir. A propósito\n'
          '     meu nome é Ayllah. Talvez nos encontremos por ai um dia.')
    linha3()
    seguir()
if derrota == False:
    print(linha2())
    print(f'{prota} segue caminho, porém, já esta chegando a tarde e sente fome,\n'
          f'{sexo[1]} encontra uma lebre.')
    print(linha2())
    print('O QUE VOCÊ FAZ?')
    sleep(0.5)

matar_coelho = int(input('[1]Matar o coelho para se alimentar\n'
                         '[2]Seguir caminho\n'))
sleep(1)
print(linha())
if matar_coelho == 1:
    print(f'Quando {prota} estava prestes a matar o coelho uma camponesa que estava caçando\n'
          f'bem perto aparece. Vendo ela que {prota} está com fome {sexo[0]} convida para almoçar\n'
          f'em sua casa!\n')
    print(linha())
    sleep(2)
    seguir()
    aleatoria = ('boa', 'ruim')
    situação = choice(aleatoria)
    if situação == 'boa':
        print(f'Após {prota} se alimentar {sexo[1]} agradece e segue com seu objetivo.\n'
              f'Ainda com sede vingança!')
    else:
        pts(3)
        print('Ao chegarem perto da vila veem fumaça no céu vindo da direção da \n'
              'vila. E quando chegam, se deparam com a vila saqueada e destruída.')
        print(linha())
        seguir()
        print('A camponesa não se contém, larga as armas e caças no chão não acreditando\n'
              'no que vê e em desespero corre para sua casa e começa a chorar lembrando\n'
              'dos seus filhos.')
        print(linha())
        seguir()
        print('Tomada pela raiva, jura matar os responsáveis.\n'
              'E pergunta se você pode ajuda-la.')
        print(linha())
        print('O QUE VOCÊ FAZ?')
        sleep(0.5)
        escolha2 = int(input('[1] Sim\n'
                         '[2] Não\n'))
        if escolha2 == 1:
            print(f'{prota} entende a dor da camponesa e ajuda a procurar os culpados.\n'
                  f'Porém...o culpado era nada mais nada menos do que o conselheiro do\n'
                  f'falecido rei Ruje chamado Acabe.')
            print(linha())
            seguir()
            print(linha())
            print('Acabe:\n'
                  f'    -Olá {prota}, não esperava lhe achar tão cedo!')
            print(linha())
            seguir()
            print(linha())
            print(f'{prota}:\n'
                  f'    -Acabe?! Foi você quem desgraçou a vida dessa pobre camponesa?\n'
                  f'    Mas, por quê?')
            print(linha())
            seguir()
            print(linha())
            print('Acabe:\n'
                  '     -Porque seu pai era um frouxo e não tinha ambição de ter todos\n'
                  '     ao seus pés!')
            seguir()
            print('     -Sim! eu matei seu pai porque ele não me ouviu!\n'
                  '     e agora você morrerá também. IDIOTA!!!!!')
            seguir()
            cabecalho('DERROTA')
            derrota = True
            print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
            input('Press enter to finish')
            exit()
        else:
            print(f'{prota} diz à pobre camponesa que não pode, pois saiu de casa em busca\n'
                  f'de vingança assim como ela fará também!')
            seguir()
            print(f'Camponesa:\n'
                  f'    -Você está certo! Esse é o meu objetivo, e somente meu! Agora que\n'
                  f'    me tiraram tudo oque eu tinha nao tenho mais porque viver!\n'
                  f'    Irei sozinha nessa missão suicida!')
pts(3)
print()
print(linha())
print(f'Ao seguir seu caminho {prota} cai em uma armadilha.')
seguir()
print(f'De repente 2 mercenarios aparecem e observando {prota} percebem que é {sexo[2]}\n'
      f'jovem formos{sexo[0]} e de saúde boa, e então decidem vendê-l{sexo[0]} como escrav{sexo[0]}\n'
      f'para ganhar um dinheiro facil.')
seguir()
print(linha())
print('LANÇAR DADOS PARA TENTAR SE SOLTAR?')
sleep(0.5)
reação = int(input('[1] Sim\n'
                 '[2] Não\n'))
if reação == 1:
    for c in range(0, 3):
        if c > 0:
            sleep(1)
            print('Tentar de novo?')
            reação2 = int(input('[1] Sim\n'
                                '[2] Não\n'))
            if reação2 == 2:
                break
        dado20 = d20()
        print('Tentando se soltar', end='')
        pts(3)
        if dado20 <= 15:
            print('\nFalhou...')
            sleep(1.5)
            if c == 0:
                cabecalho('Pode tentar mas não vai conseguir se soltar. Hahahaa!')
            elif c == 1:
                cabecalho(f'Pare garot{sexo[0]}! Você está me irritando!')
            else:
                cabecalho(f'CHEGA!!! Ess{sexo[0]} garot{sexo[0]} não vale tanto!!!')
        else:
            print('CONSEGUIU!!!')
            break
    #fazer apartir dessa linha
    print(f'{prota} corre para mais dentro ainda da floresta para fugir do alcance\n'
          f' dos mercenarios.')
    seguir()
    print(f'Ao conseguir despista-los de repente um urso selvagem de 2 metros e meio aparece\n'
          f'babando e com fome.')
    seguir()
    print(f'Você não tem escolha, terá que lutar com o urso')
    batalha()
    if decisao1 == 1:
        prota_atrb['vida'] = 13
    print(f'                Vida:{prota_atrb["vida"]:<20}  Urso:{urso["vida"]}')
    linha3(tam=75)

    while True:
        # player time
        sleep(0.5)
        print('Sua vez')
        sleep(1)
        ação = int(input('[1] Espada\n[2] Comer\n'))
        if ação == 2:  # logica para prota restaurar vida
            if prota_atrb['vida'] >= 13:
                prota_atrb['vida'] = 13
                print('Sua vida esta cheia, nao precisa comer!')
            elif prota_atrb['comida'] > 0 and -1 < prota_atrb['vida'] < 10:
                prota_atrb['comida'] -= 1
                prota_atrb['vida'] += 3
                print(f'Você ganhou +3 de vida')
                print(f'Qtd. de comida: {prota_atrb["comida"]}')
                if prota_atrb['vida'] > 10:
                    prota_atrb['vida'] = 10
            elif prota_atrb['comida'] < 0:
                print('Você não tem mais comida!')
        else:
            print('Rolando d20')
            dado20 = d20()
            sleep(1)
            tentativa = dado20 + prota_atrb['atk']
            pts(3)

            # critico ou nao
            critical = False
            if dado20 == 20:
                critical = True
                print(f'd20: {dado20} -- CRITICALL !!!')
            else:
                print(f'd20: {dado20}')
            sleep(2)
            print(f'Tentativa: {tentativa}')
            sleep(3)

            # acertou ou nao
            if tentativa >= urso['defe']:
                print(linha())
                print('Você acertou! Rolando d10')
                pts(2)
                dado10 = d10()
                print(f'{dado10} de dano')
                urso['vida'] -= dado10
                if critical:
                    print('Rolando d10 novamente')
                    pts(2)
                    dado10 = d10()
                    print(f'{dado10} de dano')
                    urso['vida'] -= dado10
                print(linha())
            else:
                erros = 'O urso desviou', 'Você errou!'
                print(choice(erros))
                print(linha())

            if urso['vida'] <= 0:
                urso['vida'] = 0
                print(f'                Vida:{prota_atrb["vida"]:<20}  Urso:{urso["vida"]}')
                linha3(tam=75)
                break
        sleep(2)
        print(f'                Vida:{prota_atrb["vida"]:<20}  Urso:{urso["vida"]}')
        linha3(tam=75)

        # enemy time
        sleep(0.5)
        print('Vez do urso')
        sleep(1)
        print('Rolando d20')
        dado20 = d20()
        sleep(1)
        tentativa = dado20 + urso['atk']
        pts(3)

        # critico ou nao
        critical = False
        if dado20 == 20:
            critical = True
            print(f'd20: {dado20} -- CRITICALL !!!')
        else:
            print(f'd20: {dado20}')
        sleep(2)
        print(f'Tentativa: {tentativa}')
        sleep(3)

        # acertou ou nao
        if tentativa >= prota_atrb['defe']:
            print('O urso acertou! Rolando d10')
            pts(2)
            dado10 = d10()
            print(f'{dado10} de dano')
            prota_atrb["vida"] -= dado10
            if critical:
                print('rolando d10 novamente')
                pts(2)
                dado10 = d10()
                print(f'{dado10} de dano')
                prota_atrb["vida"] -= dado10
            print(linha())
        else:
            erros = 'Você desviou', 'O urso errou!'
            print(choice(erros))
            print(linha())

        if prota_atrb['vida'] <= 0:
            prota_atrb['vida'] = 0
            print(f'                Vida:{prota_atrb["vida"]:<20}  Uros:{urso["vida"]}')
            linha3(tam=75)
            break
        sleep(2)
        print(f'                Vida:{prota_atrb["vida"]:<20}  Urso:{urso["vida"]}')
        linha3(tam=75)

    if urso['vida'] <= 0:
        cabecalho('VITORIA')
        input('Press enter to finish')
    else:
        cabecalho('DERROTA')
        derrota = True
        print('Você morreu! Sua sede de vingança foi responsável pela sua destruição.')
        input('Press enter to finish')
        exit()
    print('Depois de obter exito na luta contra o urso e ja anoitecendo, você avista\n'
          'o que poderia ser um reino entre algumas brechas da floresta.')
    continua()
    seguir()
else:
    print('Durante a caminhada os mercenarios perguntam oque você fazia na floresta.\n'
          'E você responde. Entao um deles diz que você nunca conseguiria entrar la\n'
          'porque precisaria de uma autorização da sua entrada.')
    seguir()
    print('Ao fim da tarde logo chegam nas proximidades do reino LEMSA.')
    seguir()
    print('O que será que vai acontecer?')
    continua()