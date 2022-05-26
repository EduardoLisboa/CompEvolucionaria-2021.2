class Materia:
    def __init__(self, nome, codigo, carga_horaria, periodo=None, prereqs=None):
        self.nome = nome
        self.codigo = codigo
        self.carga_horaria = carga_horaria
        self.periodo = periodo
        self.prereqs = prereqs

    def pegar_codigo(self):
        return self.codigo

    def pegar_prereqs(self):
        return self.prereqs

    def pegar_carga_horaria(self):
        return self.carga_horaria

    def pegar_periodo(self):
        return self.periodo if self.periodo != 11 else 0

    def eh_eletiva(self):
        return True if self.periodo == 10 else False

    def eh_extensao(self):
        return True if self.periodo == 11 else False

    def eh_obrigatoria(self):
        return True if self.periodo != 10 and self.periodo != 11 else False

    def __eq__(self, other):
        return self.codigo == other.codigo if isinstance(other, Materia) else self.codigo == other

    def __repr__(self):
        if self.periodo == 10:
            info_periodo = 'Eletiva'
        elif self.periodo == 11:
            info_periodo = 'Extensão'
        else:
            info_periodo = self.periodo

        return f'{self.nome} - {self.codigo} - {info_periodo}'


CARGA_HORARIA_FIXA = 2016
CARGA_HORARIA_ELETIVA = 936
CARGA_HORARIA_FLEXIVEL = 240
CARGA_HORARIA_TCC = 180
CARGA_HORARIA_EXTENSAO = 375

disciplinas_obrigatorias = [
    Materia('Programação 1', 'COMP359', 72, 1),
    Materia('Lógica para Computação', 'COMP360', 72, 1),
    Materia('Computação, Sociedade e Ética', 'COMP361', 72, 1),
    Materia('Matemática Discreta', 'COMP362', 72, 1),
    Materia('Cálculo Diferencial e Integral', 'COMP363', 144, 1),
    Materia('Estrutura de Dados', 'COMP364', 72, 2),
    Materia('Banco de Dados', 'COMP365', 72, 2),
    Materia('Organização e Arquitetura de Computadores', 'COMP366', 72, 2),
    Materia('Geometria Analítica', 'COMP367', 72, 2),
    Materia('Redes de Computadores', 'COMP368', 72, 3),
    Materia('Teoria dos Grafos', 'COMP369', 72, 3),
    Materia('Probabilidade e Estatística', 'COMP370', 72, 3),
    Materia('Álgebra Linear', 'COMP371', 72, 3),
    Materia('Programação 2', 'COMP372', 72, 4),
    Materia('Programação 3', 'COMP373', 72, 4),
    Materia('Projeto e Análise de Algoritmos', 'COMP374', 72, 4, ['COMP364', 'COMP369']),
    Materia('Teoria da Computação', 'COMP376', 72, 4),
    Materia('Sistemas Operacionais', 'COMP378', 72, 5),
    Materia('Compiladores', 'COMP379', 72, 5),
    Materia('Inteligência Artificial', 'COMP380', 72, 5),
    Materia('Computação Gráfica', 'COMP381', 72, 5),
    Materia('Projeto e Desenvolvimento de Sistemas', 'COMP382', 288, 6),
    Materia('Metodologia de Pesquisa e Trabalho Individual', 'COMP386', 72, 7),
    Materia('Noções de Direito', 'COMP387', 72, 7)
]

disciplinas_extensao = [
    Materia('ACE 1: Projeto 1', 'COMP377', 75, 11),
    Materia('ACE 2: Continuidade do Projeto 1', 'COMP383', 75, 11),
    Materia('ACE 3: Projeto 2', 'COMP384', 75, 11),
    Materia('ACE 4: Continudade do Projeto 2', 'COMP388', 75, 11),
    Materia('ACE 5: Evento', 'COMP385', 75, 11)
]

disciplinas_eletivas = [
    Materia('Conceitos de Linguagem de Programação', 'COMP389', 72, 10),
    Materia('Aprendizagem de Máquina', 'COMP390', 72, 10),
    Materia('Sistemas Digitas', 'COMP391', 72, 10),
    Materia('Sistemas Distribuídos', 'COMP392', 72, 10),
    Materia('Redes Neurais e Aprendizado Profundo', 'COMP393', 72, 10),
    Materia('FPGA', 'COMP394', 72, 10),
    Materia('Interação Homem-Máquina', 'COMP395', 72, 10),
    Materia('Processamento Digital de Imagens', 'COMP396', 72, 10),
    Materia('Computação Evolucionária', 'COMP397', 72, 10),
    Materia('Sistemas Embarcados', 'COMP398', 72, 10),
    Materia('Gerência de Projeto', 'COMP399', 72, 10),
    Materia('Visão Computacional', 'COMP400', 72, 10),
    Materia('Ciência de Dados', 'COMP401', 72, 10),
    Materia('Microcontroladores e Aplicações', 'COMP402', 72, 10),
    Materia('Segurança de Sistemas Computacionais', 'COMP403', 72, 10),
    Materia('Cálculo 3', 'COMP404', 72, 10),
    Materia('Navegação em Robótica Móvel', 'COMP417', 72, 10),
    Materia('Pesquisa Operacional', 'COMP418', 72, 10),
    Materia('Cálculo 2', 'COMP419', 72, 10),
    Materia('Empreendedorismo', 'COMP420', 72, 10),
    Materia('Introdução à Computação', 'COMP421', 72, 10),
    Materia('Teste de Software', 'COMP422', 72, 10),
    Materia('Banco de Dados 2', 'COMP423', 40, 10),
    Materia('Fundamentos de IA Aplicados ao Diagnóstico Médico', 'COMP424', 72, 10),
    Materia('Processamento de Linguagem Natural', 'COMP425', 72, 10),
    Materia('Laboratório de Programação', 'COMP426', 40, 10),
    Materia('Inteligência Artificial Aplicada ao Diagnóstico de Doenças', 'COMP428', 72, 10),
    Materia('Cálculo 4', 'COMP429', 72, 10),
    Materia('Tópicos em Software Básico', 'COMP430', 72, 10),
    Materia('Libras', 'COMP431', 72, 10),
    Materia('Gamificação', 'COMP433', 72, 10),
    Materia('Exploração e Mineração de Dados', 'COMP434', 72, 10),
    Materia('Tópicos Especiais em Gestão de Projetos', 'COMP435', 72, 10),
    Materia('Tópicos Especiais em Banco de Dados: Gerência de Dados Semiestruturados', 'COMP436', 72, 10),
    Materia('Tópicos em Engenharia de Software: Projetando Linhas de Produto de Software', 'COMP437', 72, 10),
    Materia('Cálculo 1', 'COMP439', 72, 10)
]

enfases = {
    'Computação Visual': ['COMP404', 'COMP390', 'COMP393', 'COMP396', 'COMP400'],
    'Sistemas Inteligentes': ['COMP404', 'COMP390', 'COMP393', 'COMP397', 'COMP401'],
    'Sistemas De Computação': ['COMP404', 'COMP391', 'FPGA', 'COMP398', 'COMP402'],
    'Sistemas De Informação': ['COMP389', 'COMP392', 'COMP395', 'COMP399', 'COMP403']
}
