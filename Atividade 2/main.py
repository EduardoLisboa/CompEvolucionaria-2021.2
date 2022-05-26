import materias
import math
import random
import time


class Aluno:
    def __init__(self, periodo, pagas, conceito_pagas, pagando, a_pagar, enfase=None):
        self.ch_fixa = 0
        self.ch_eletiva = 0
        self.ch_extensao = 0
        self.periodo_atual = periodo
        self.periodos_restantes = 12 - periodo
        self.materias_pagas = pagas
        self.conceito_materias_pagas = conceito_pagas
        self.materias_pagando = pagando
        self.materias_a_pagar = a_pagar
        self.enfase = enfase
        self.materias_enfase = None

    def carga_horaria_faltante(self):
        print(f'Carga Horária Cumprida:\n'
              f'\tFixa - {self.ch_fixa}\n'
              f'\tEletiva - {self.ch_eletiva}\n'
              f'\tExtensão - {self.ch_extensao}')
        print(f'Carga Horária Faltante:\n'
              f'\tFixa - {materias.CARGA_HORARIA_FIXA - self.ch_fixa}\n'
              f'\tEletiva - {materias.CARGA_HORARIA_ELETIVA - self.ch_eletiva}\n'
              f'\tExtensão - {materias.CARGA_HORARIA_EXTENSAO - self.ch_extensao}')

    def __repr__(self):
        return f"Periodo: {self.periodo_atual}\n" \
               f"Períodos Restantes: {self.periodos_restantes}\n" \
               f"Materias pagas: {self.materias_pagas}\n" \
               f"Materias pagando: {self.materias_pagando}\n" \
               f"Materias à pagar: {self.materias_a_pagar}\n" \
               f"Ênfase desejada: {'Nenhuma' if self.enfase is None else self.enfase}"


def ler_dados_aluno():
    dados_entrada = dict()
    entrada_completa = list()

    with open('entrada.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            entrada_completa.append(line[:-1])

    for index, linha in enumerate(entrada_completa):
        entrada = linha.split(':')[1].split()
        if index > 0:
            for i, item in enumerate(entrada):
                if ',' in item:
                    entrada[i] = item[:-1]
        dados_entrada[index] = entrada

    dados_entrada[0] = int(dados_entrada[0][0])
    dados_entrada[5] = ' '.join(dados_entrada[5]).title()

    return Aluno(*dados_entrada.values())


def processamento_inicial_aluno(aluno):
    materias_da_enfase = materias.enfases[aluno.enfase][:]

    # Considerar materias pagando como matérias pagas e aprovadas
    for mat in aluno.materias_pagando:
        if mat in aluno.materias_a_pagar:
            aluno.materias_a_pagar.remove(mat)
            aluno.materias_pagas.append(mat)
            aluno.conceito_materias_pagas.append('AP')
        for i in range(0, len(materias.disciplinas_eletivas)):
            if materias.disciplinas_eletivas[i].pegar_codigo() == mat:
                if mat in materias_da_enfase:
                    materias_da_enfase.remove(mat)
                aluno.materias_pagas.append(mat)
                aluno.conceito_materias_pagas.append('AP')

    aluno.materias_enfase = materias_da_enfase[:]

    # Ajustar matérias à pagar e pagas e carga horária cumprida
    for index, mat in enumerate(aluno.materias_pagas):
        if aluno.conceito_materias_pagas[index] != 'AP':
            for i in range(0, len(materias.disciplinas_obrigatorias)):
                if materias.disciplinas_obrigatorias[i].pegar_codigo() == mat:
                    aluno.materias_a_pagar.append(mat)
                    print(f'Disciplina a pagar novamente: {mat}')
        elif aluno.conceito_materias_pagas[index] == 'AP':
            for i in range(0, len(materias.disciplinas_obrigatorias)):
                if materias.disciplinas_obrigatorias[i].pegar_codigo() == mat:
                    aluno.ch_fixa += materias.disciplinas_obrigatorias[i].carga_horaria

            for i in range(0, len(materias.disciplinas_eletivas)):
                if materias.disciplinas_eletivas[i].pegar_codigo() == mat:
                    aluno.ch_eletiva += materias.disciplinas_eletivas[i].carga_horaria

            for i in range(0, len(materias.disciplinas_extensao)):
                if materias.disciplinas_extensao[i].pegar_codigo() == mat:
                    aluno.ch_extensao += materias.disciplinas_extensao[i].carga_horaria


def gerar_pop_inicial(aluno):
    pop_inicial = list()

    qtd_materias_obrigatorias = 24
    qtd_materias_eletivas = 14

    obrigatorias_faltantes = list()
    eletivas_faltantes = list()

    for mat in materias.disciplinas_obrigatorias:
        if mat not in aluno.materias_pagas:
            obrigatorias_faltantes.append(mat)
        else:
            qtd_materias_obrigatorias -= 1

    for mat in materias.disciplinas_eletivas:
        if mat not in aluno.materias_pagas:
            eletivas_faltantes.append(mat)
        else:
            qtd_materias_eletivas -= 1

    while len(pop_inicial) < 20:
        plano_de_curso = list()

        random.shuffle(obrigatorias_faltantes)
        plano_de_curso.extend(obrigatorias_faltantes[:])
        plano_de_curso.extend(random.sample(eletivas_faltantes, k=qtd_materias_eletivas))

        plano_de_curso_ok = list()
        passo = math.ceil(len(plano_de_curso) / aluno.periodos_restantes)
        for i in range(0, len(plano_de_curso), passo):
            aux = plano_de_curso[i:i+passo]
            plano_de_curso_ok.append(aux[:])

        periodo_extensao = len(plano_de_curso_ok) - 5
        for index, mat in enumerate(materias.disciplinas_extensao, start=periodo_extensao):
            plano_de_curso_ok[index].append(mat)

        pop_inicial.append(plano_de_curso_ok[:])

    return pop_inicial


def adaptacao(pop_inicial, aluno):
    adapt = list()

    for plano_de_curso in pop_inicial:
        adapt_genoma = 0

        cargas_horarias = {
            'obrigatoria': materias.CARGA_HORARIA_FIXA,
            'eletiva': materias.CARGA_HORARIA_ELETIVA,
            'extensao': materias.CARGA_HORARIA_EXTENSAO
        }

        materias_da_enfase = aluno.materias_enfase[:]
        materia_com_prereqs = list()
        for index, per in enumerate(plano_de_curso):
            # Checagem do periodo da materia em relação ao período em que ela foi inserida
            for mat in per:
                adapt_genoma -= abs((mat.pegar_periodo() - (aluno.periodo_atual + index + 1))) ** 2

            # Contabilizando pré-requisitos
            for mat in per:
                if mat.prereqs:
                    materia_com_prereqs.append([index, mat])

            # Checagem das materias eletivas da ênfase escolhida
            for mat in per:
                if mat in materias_da_enfase:
                    materias_da_enfase.remove(mat.pegar_codigo())

            # Checagem da carga horária total
            for mat in per:
                if mat.eh_obrigatoria():
                    cargas_horarias['obrigatoria'] -= mat.carga_horaria
                if mat.eh_eletiva():
                    cargas_horarias['eletiva'] -= mat.carga_horaria
                if mat.eh_extensao():
                    cargas_horarias['extensao'] -= mat.carga_horaria

        # Continuação da checagem dos pré-requisitos
        for index_per, mat in materia_com_prereqs:
            prereqs = mat.prereqs[:]
            copy_prereqs = prereqs[:]
            for prereq in prereqs:
                if prereq not in aluno.materias_pagas:
                    if index_per == 0:
                        adapt_genoma -= 10000
                    else:
                        for i in range(0, index_per):
                            for mat_mat in plano_de_curso[i]:
                                if mat_mat in prereqs:
                                    copy_prereqs.remove(mat_mat)
                else:
                    copy_prereqs.remove(prereq)

            if copy_prereqs:
                adapt_genoma -= 10000

        # Pontuação da ênfase
        adapt_genoma -= len(materias_da_enfase) ** 10

        cargas_horarias['obrigatoria'] -= aluno.ch_fixa
        cargas_horarias['eletiva'] -= aluno.ch_eletiva
        cargas_horarias['extensao'] -= aluno.ch_extensao

        # Pontuação da carga horária
        for ch in cargas_horarias.values():
            if ch > 0:
                adapt_genoma -= 10000

        adapt.append([adapt_genoma, plano_de_curso[:]])

    return adapt


def mutacao(populacao, aluno):
    nova_populacao = list()
    for plano_de_curso in populacao:
        mutar = random.randint(1, 100)
        novo_plano_de_curso = plano_de_curso[:]
        if mutar <= 5:
            indice1 = random.randint(0, len(plano_de_curso) // 2)
            indice2 = random.randint(len(plano_de_curso) // 2, len(plano_de_curso) - 1)

            cara_ou_coroa = random.randint(0, 1)
            if cara_ou_coroa:
                aux = novo_plano_de_curso[indice1][:]
                novo_plano_de_curso[indice1] = novo_plano_de_curso[indice2][:]
                novo_plano_de_curso[indice2] = aux[:]

                aces_info = list()
                for index_per, per in enumerate(novo_plano_de_curso):
                    for index_mat, mat in enumerate(per):
                        if mat in materias.disciplinas_extensao:
                            aces_info.append([index_per, mat])

                for index_per, mat in aces_info:
                    novo_plano_de_curso[index_per].remove(mat)

                periodo_extensao = len(novo_plano_de_curso) - 5
                for index, mat in enumerate(materias.disciplinas_extensao, start=periodo_extensao):
                    novo_plano_de_curso[index].append(mat)

        materias_da_enfase = aluno.materias_enfase[:]
        for per in plano_de_curso:
            for mat in per:
                if mat in materias_da_enfase:
                    materias_da_enfase.remove(mat.pegar_codigo())

        for index_per, per in enumerate(plano_de_curso):
            for index_mat, mat in enumerate(per):
                if mat not in materias_da_enfase and mat.eh_eletiva():
                    for elet in materias.disciplinas_eletivas:
                        if elet in materias_da_enfase:
                            novo_plano_de_curso[index_per][index_mat] = elet
                            materias_da_enfase.remove(elet.pegar_codigo())
                            break

        nova_populacao.append(novo_plano_de_curso[:])

    return nova_populacao


def main():
    aluno = ler_dados_aluno()
    processamento_inicial_aluno(aluno)

    pop_inicial = gerar_pop_inicial(aluno)

    adaptacao_inicial = adaptacao(pop_inicial, aluno)
    adaptacao_inicial.sort(key=lambda x: x[0], reverse=True)

    adapt_pop = pop_inicial[:]

    limite_de_geracoes = 100
    adaptacao_nova_pop = list()

    # Loop principal
    for i in range(0, limite_de_geracoes):
        print(f'GERAÇÃO {i + 1}')
        print(f'-=-=- {"FAZENDO MUTAÇÕES":^25} -=-=-')
        pop = mutacao(adapt_pop, aluno)

        print(F'-=-=- {"CALCULANDO NOVA ADAPTAÇÃO":^25} -=-=-')
        adaptacao_nova_pop = adaptacao(pop, aluno)
        adaptacao_nova_pop.sort(key=lambda x: x[0], reverse=True)

        adapt_pop = [plano[1] for plano in adaptacao_nova_pop]
        # adapt_pop.extend(pop[:5])

        print()
        time.sleep(0.02)

    # Exibição dos resultados
    melhores_3 = [adaptacao_nova_pop[i][:] for i in range(0, 3)]

    print(f'\n\n-=-=-=-  FIM  -=-=-=-\n')
    time.sleep(1)
    print(f'Melhores adaptações: {melhores_3[0][0]}, {melhores_3[1][0]} e {melhores_3[2][0]}\n')
    time.sleep(1)

    print('MATÉRIAS JÁ PAGAS:')
    for mat in materias.disciplinas_obrigatorias:
        if mat in aluno.materias_pagas:
            print(f'\t{mat}')
    for mat in materias.disciplinas_eletivas:
        if mat in aluno.materias_pagas:
            print(f'\t{mat}')
    for mat in materias.disciplinas_extensao:
        if mat in aluno.materias_pagas:
            print(f'\t{mat}')
    print()

    for num_plano, melhor in enumerate(melhores_3, start=1):
        print(f'PLANO DE CURSO {num_plano}')
        for index, per in enumerate(melhor[1], start=aluno.periodo_atual+1):
            print(f'\tPeríodo: {index}')
            for mat in per:
                print(f'\t\t{mat}')
        print()
        time.sleep(1)


if __name__ == '__main__':
    main()
