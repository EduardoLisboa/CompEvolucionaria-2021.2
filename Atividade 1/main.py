"""
Atividade 1 para 1 ABN

Atividade realizada na linguagem Python, versão 3.9
Para fazer funcionar, rodar o arquivo "main.py", com o arquivo "ambientes.py" na mesma pasta

Nome: Eduardo Antônio de Lucena Lisboa
        48      65    10   46     54

- Quantidade de andares:
    Eduardo = 48
    Resultado = 48 % 3 = 0
    - 1 andar

- Forma da casa:
    Antônio = 65
    Resultado = 65 % 2 = 1
    - Casa retangular

- Ambiente especial:
    de = 10
    Resultado = 10 % 3 = 1
    - Sala de jogos

- Outros ambientes:
    Lucena = 46
    Resultado = 10 % 3 = 1
    - 2 quartos, 2 banheiros, 2 closet e 1 lavanderia

Instruções e restrições:
    - Toda casa deve ter uma cozinha, sala de estar e sala de jantar.
    - Pelo menos uma porta e uma janela em cada cômodo.

    - Quarto --------- 12 a 30 m^2
    - Banheiro -------  3 a  8 m^2
    - Cozinha -------- 10 a 15 m^2
    - Escritório -----  6 a 10 m^2
    - Lavanderia -----  6 a 10 m^2
    - Sala de jogos -- 20 a 30 m^2
    - Closet ---------  3 a  4 m^2
    - Sala de estar -- 30 a 40 m^2
    - Sala de jantar - 15 a 20 m^2


Minha casa:
    - 1 andar
    - Sala de estar
    - Sala de jantar
    - Cozinha
    - Sala de jogos
    - 2 quartos
    - 2 banheiros
    - 2 closets
    - Lavanderia

Sala de estar: 8x5
SE----+
|     |
|     |
|     |
|     |
|     |
|     |
|     |
|     |
+-----+

Sala de jantar: 5x4
SJA--+
|    |
|    |
|    |
|    |
|    |
+----+

Cozinha: 3x5
CO----+
|     |
|     |
|     |
+-----+

Sala de Jogos: 6x4
SJO--+
|    |
|    |
|    |
|    |
|    |
|    |
+----+

Quarto: 4x4 (2)
Q----+
|    |
|    |
|    |
|    |
+----+

Banheiro: 2x2 (2)
B--+
|  |
|  |
+--+

Closet: 2x2 (2)
CL-+
|  |
|  |
+--+

Lavandeira: 3x3 (2)
L---+
|   |
|   |
|   |
+---+


Casa Ideal:
CL-+Q----+SE----+SJO--+
|  ||    ||     ||    |
|  ||    ||     ||    |
+--+|    ||     ||    |
B--+|    ||     ||    |
|  ||    ||     ||    |
|  ||    ||     ||    |
+--++----+|     ||    |
B--+Q----+|     ||    |
|  ||    ||     ||    |
|  ||    ||     ||    |
+--+|    ||     ||    |
CL-+|    ||     |+----+
|  ||    ||     |SJA--+
|  ||    ||     ||    |
+--++----++-----+|    |
L---+L---+CO----+|    |
|   ||   ||     ||    |
|   ||   ||     ||    |
|   ||   ||     ||    |
+---++---++-----++----+

"""

import random
from time import sleep
import ambientes


def gerar_pop(tamanho):
    pop_inicial = list()

    lista_ambientes = ambientes.ambientes[:]

    for _ in range(tamanho):
        aux_ambientes = list()
        while len(aux_ambientes) != 12:
            portas = [random.randint(0, 2) for _ in range(0, 4)]
            janelas = [random.randint(0, 1) for _ in range(0, 4)]
            aux_ambientes.append(random.choice(lista_ambientes)(portas, janelas))

        pop_inicial.append(aux_ambientes[:])

    return pop_inicial


def adaptacao(populacao, casa_ideal):
    pop_adaptacao = list()

    for casa in populacao:
        # Adaptação da posição dos ambientes
        adapt_posicao_ambiente = 0
        for i in range(0, 12):
            if casa[i].nome == casa_ideal[i].nome:
                adapt_posicao_ambiente += 1
            else:
                adapt_posicao_ambiente -= 1

        # Adaptação da quantidade de ambientes
        qtd_ambientes = ambientes.qtd_ideal_ambientes.copy()
        for i in range(0, 12):
            qtd_ambientes[casa[i].nome] -= 1

        qtd_certa = 0
        for i in range(0, 12):
            if qtd_ambientes[casa[i].nome] == 0:
                qtd_certa += 1

        adapt_qtd_ambientes = 0
        if qtd_certa == 12:
            adapt_qtd_ambientes = 12
        else:
            for i in range(0, 12):
                if qtd_ambientes[casa[i].nome] >= 0:
                    adapt_qtd_ambientes += qtd_ambientes[casa[i].nome] * 2
                elif qtd_ambientes[casa[i].nome] < 0:
                    adapt_qtd_ambientes += qtd_ambientes[casa[i].nome] * -2

            adapt_qtd_ambientes *= -1

        # Adaptação da quantidade de portas e janelas
        adapt_qtd_portas = qtd_certa_portas = 0
        adapt_qtd_janelas = qtd_certa_janelas = 0

        direcoes = ['cima', 'baixo', 'esquerda', 'direita']
        for ambiente in range(0, 12):
            for direcao in direcoes:
                if casa[ambiente].portas[direcao] == casa_ideal[ambiente].portas[direcao]:
                    qtd_certa_portas += 1
                if casa[ambiente].janelas[direcao] == casa_ideal[ambiente].janelas[direcao]:
                    qtd_certa_janelas += 1

        # print(qtd_certa_portas, qtd_certa_janelas)
        qtd_certa_portas //= 4
        qtd_certa_janelas //= 4

        if qtd_certa_portas == 12:
            adapt_qtd_portas = 12
        else:
            adapt_qtd_portas = qtd_certa_portas * -2

        if qtd_certa_janelas == 12:
            adapt_qtd_janelas = 12
        else:
            adapt_qtd_janelas = qtd_certa_janelas * -2

        # print(adapt_qtd_portas, adapt_qtd_janelas)

        adapt = adapt_posicao_ambiente + adapt_qtd_ambientes + adapt_qtd_portas + adapt_qtd_janelas

        pop_adaptacao.append([adapt, casa])

    pop_nova_adaptacao = list(map(lambda x: [x[0]**2 if x[0] > 0 else -1*(x[0]**2), x[1]], pop_adaptacao))
    pop_nova_adaptacao.sort(key=lambda x: x[0], reverse=True)
    # for adapt in pop_nova_adaptacao:
    #     print(adapt)

    return pop_nova_adaptacao


def mutacao(populacao, casa_ideal):
    nova_pop = list()

    lista_ambientes = ambientes.ambientes[:]

    for casa in populacao:
        indices_mutaveis = [i for i in range(0, 12) if casa[1][i].nome != casa_ideal[i].nome]
        limite_maximo = len(indices_mutaveis) - 1
        if len(indices_mutaveis) > 1:
            indices_aleatorios = [random.randint(0, limite_maximo) for _ in range(0, random.randint(1, limite_maximo))]
        else:
            indices_aleatorios = [random.randint(0, 11) for _ in range(0, 3)]

        indices_aleatorios = list(set(indices_aleatorios))
        indices_aleatorios.sort()

        # Mutar ambientes para novos ambientes
        for i in indices_aleatorios:
            cara_ou_coroa = random.randint(0, 1)
            if cara_ou_coroa:
                portas = list(casa[1][i].portas.values())
                janelas = list(casa[1][i].janelas.values())
                novo_ambiente = random.choice(lista_ambientes)(portas, janelas)
                while novo_ambiente.nome == casa[1][i].nome:
                    novo_ambiente = random.choice(lista_ambientes)(portas, janelas)
                casa[1][i] = novo_ambiente

        # Trocar ambientes entre si
        if len(indices_mutaveis) > 1:
            cara_ou_coroa = random.randint(0, 1)
            if cara_ou_coroa:
                indice_1 = random.choice(indices_mutaveis)
                indice_2 = random.choice(indices_mutaveis)
                while indice_2 == indice_1:
                    indice_2 = random.choice(indices_mutaveis)

                if indice_2 < indice_1:
                    indice_1, indice_2 = indice_2, indice_1

                casa[1][indice_1], casa[1][indice_2] = casa[1][indice_2], casa[1][indice_1]

        # Mutar quantidade de portas e janelas
        direcoes = ['cima', 'baixo', 'esquerda', 'direita']
        for ambiente in range(0, 12):
            for direcao in direcoes:
                qtd_portas_atual = casa[1][ambiente].portas[direcao]
                if qtd_portas_atual != casa_ideal[ambiente].portas[direcao]:
                    qtd_portas_nova = random.randint(0, 2)
                    while qtd_portas_nova == qtd_portas_atual:
                        qtd_portas_nova = random.randint(0, 2)
                    casa[1][ambiente].portas[direcao] = qtd_portas_nova

                if casa[1][ambiente].janelas[direcao] != casa_ideal[ambiente].janelas[direcao]:
                    casa[1][ambiente].janelas[direcao] = random.randint(0, 1)

        nova_pop.append(casa[1][:])

    return nova_pop


def imprimir_casa(casa):
    planta_baixa = [[' ' for _ in range(0, 23)] for _ in range(0, 21)]
    x_y = [
        [0, 0, 4, 4],      # Closet
        [4, 0, 8, 4],      # Banheiro
        [8, 0, 12, 4],     # Banheiro
        [12, 0, 16, 4],    # Closet
        [16, 0, 21, 5],    # Lavanderia
        [0, 4, 8, 10],     # Quarto
        [8, 4, 16, 10],    # Quarto
        [16, 5, 21, 10],   # Lavanderia
        [0, 10, 16, 17],   # Sala de Estar
        [16, 10, 21, 17],  # Cozinha
        [0, 17, 12, 23],    # Sala de Jogos
        [12, 17, 21, 23]    # Sala de Jantar
    ]
    for ambiente in casa:
        if ambiente.portas['cima'] == 1:
            ambiente.forma[0][1] = '['
            ambiente.forma[0][2] = ']'
        if ambiente.portas['baixo'] == 1:
            ambiente.forma[len(ambiente.forma)-1][1] = '['
            ambiente.forma[len(ambiente.forma)-1][2] = ']'
        if ambiente.portas['esquerda'] == 1:
            ambiente.forma[1][0] = '-'
            ambiente.forma[2][0] = '-'
        if ambiente.portas['esquerda'] == 2:
            ambiente.forma[1][0] = '-'
            ambiente.forma[2][0] = '-'
            ambiente.forma[len(ambiente.forma)-3][0] = '-'
            ambiente.forma[len(ambiente.forma)-2][0] = '-'
        if ambiente.portas['direita'] == 1:
            ambiente.forma[1][len(ambiente.forma[0])-1] = '-'
            ambiente.forma[2][len(ambiente.forma[0])-1] = '-'
        if ambiente.portas['direita'] == 2:
            ambiente.forma[1][len(ambiente.forma[0])-1] = '-'
            ambiente.forma[2][len(ambiente.forma[0])-1] = '-'
            ambiente.forma[len(ambiente.forma)-3][len(ambiente.forma[0])-1] = '-'
            ambiente.forma[len(ambiente.forma)-2][len(ambiente.forma[0])-1] = '-'

        if ambiente.janelas['cima'] == 1:
            ambiente.forma[0][1] = '{'
            ambiente.forma[0][2] = '}'
        if ambiente.janelas['baixo'] == 1:
            ambiente.forma[len(ambiente.forma)-1][1] = '{'
            ambiente.forma[len(ambiente.forma)-1][2] = '}'
        if ambiente.janelas['esquerda'] == 1:
            ambiente.forma[1][0] = '~'
            ambiente.forma[2][0] = '~'
        if ambiente.janelas['direita'] == 1:
            ambiente.forma[1][ambiente.w+1] = '~'
            ambiente.forma[2][ambiente.w+1] = '~'

    for indice, ambiente in enumerate(casa):
        x, y = x_y[indice][0], x_y[indice][1]
        h, w = x_y[indice][2], x_y[indice][3]
        i = 0
        for row in range(x, h):
            j = 0
            for col in range(y, w):
                planta_baixa[row][col] = ambiente.forma[i][j]
                j += 1
            i += 1

    with open('Resultados.txt', 'a') as f:
        f.write('\nPLANTA BAIXA\n')
        for row in planta_baixa:
            for col in row:
                f.write(col)
                print(col, end='')
            f.write('\n')
            print()

        print('\nLegenda:')
        print('  [] ou = : porta')
        print('  {} ou ≈ : janela')
        print('     B    : banheiro')
        print('     CL   : closet')
        print('     CO   : cozinha')
        print('     L    : lavanderia')
        print('     Q    : quarto')
        print('     SE   : sala de estar')
        print('     SJA  : sala de jantar')
        print('     SJO  : sala de jogos')

        f.write('\n\nLegenda:\n')
        f.write('  [] ou = : porta\n')
        f.write('  {} ou ~ : janela\n')
        f.write('     B    : banheiro\n')
        f.write('     CL   : closet\n')
        f.write('     CO   : cozinha\n')
        f.write('     L    : lavanderia\n')
        f.write('     Q    : quarto\n')
        f.write('     SE   : sala de estar\n')
        f.write('     SJA  : sala de jantar\n')
        f.write('     SJO  : sala de jogos\n')


def main():
    casa_ideal = ambientes.casa_ideal[:]

    pop_inicial = gerar_pop(50)

    adaptacao_pop_inicial = adaptacao(pop_inicial, casa_ideal)
    adaptacao_pop = adaptacao_pop_inicial.copy()

    geracao = 0
    limite_de_geracoes = 5000
    atingiu_limite = False

    with open('Resultados.txt', 'w') as f:
        print('Arquivo de resultados criado')

    while adaptacao_pop[0][0] != 2304:
        geracao += 1
        if geracao > limite_de_geracoes:
            atingiu_limite = True
            break
        print(f'Geração {geracao}')

        print('-=-=- ESCOLHENDO MELHORES DA GERAÇÃO ANTERIOR -=-=-')
        melhores = adaptacao_pop[:25]

        print('-=-=- GERANDO NOVA POPULAÇÃO -=-=-')
        nova_pop = mutacao(melhores, casa_ideal)

        print('-=-=- CALCULANDO ADAPTAÇÃO -=-=-')
        adaptacao_nova_pop = adaptacao(nova_pop, casa_ideal)

        print('-=-=- JUNTANDO AS POPULAÇÕES -=-=-')
        adaptacao_total = melhores[:]
        adaptacao_total.extend(adaptacao_nova_pop)
        adaptacao_total.sort(key=lambda x: x[0], reverse=True)

        adaptacao_pop = adaptacao_total.copy()

        print(f'Melhor fitness da geração atual: {adaptacao_pop[0][0]}')

        with open('Resultados.txt', 'a', encoding='utf-8') as f:
            f.write(f'GERAÇÃO {geracao}\n')
            f.write(f'Melhor fitness: {adaptacao_pop[0][0]}\n')
            f.write(f'Casa com melhor fitness:\n')
            for ambiente in adaptacao_pop[0][1]:
                f.write(f'    {ambiente.nome.title():>14} - ')
                f.write(f'Portas = {list(ambiente.portas.values())} - ')
                f.write(f'Janelas = {list(ambiente.janelas.values())}\n')
            f.write('\n')

        print()
        sleep(0.005)

    if atingiu_limite:
        print('O limite de gerações foi atingido')
        print(f'O melhor fitness foi: {adaptacao_pop[0][0]}')
        print('E a melhor casa foi:')
        for ambiente in adaptacao_pop[0][1]:
            print(f'    {ambiente.nome.title()}')
    else:
        print(f'Casa encontrada na geração {geracao}!')
        print(f'O melhor fitness foi: {adaptacao_pop[0][0]}')
        print('E a melhor casa foi:')
        for ambiente in adaptacao_pop[0][1]:
            print(f'    {ambiente.nome.title()}')

    print()
    imprimir_casa(adaptacao_pop[0][1])


if __name__ == '__main__':
    main()
