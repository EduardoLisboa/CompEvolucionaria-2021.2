class Ambiente:
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        self.portas = {
            'cima':     portas[0],
            'baixo':    portas[1],
            'esquerda': portas[2],
            'direita':  portas[3]
        }
        self.janelas = {
            'cima':     janelas[0],
            'baixo':    janelas[1],
            'esquerda': janelas[2],
            'direita':  janelas[3]
        }


class Banheiro(Ambiente):
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        super().__init__(portas, janelas)
        self.nome = 'banheiro'
        self.h = 2
        self.w = 2
        self.forma = [
            ['+', '-', '-', '+'],
            ['|', 'B', ' ', '|'],
            ['|', ' ', ' ', '|'],
            ['+', '-', '-', '+']
        ]


class Closet(Ambiente):
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        super().__init__(portas, janelas)
        self.nome = 'closet'
        self.h = 2
        self.w = 2
        self.forma = [
            ['+', '-', '-', '+'],
            ['|', 'C', 'L', '|'],
            ['|', ' ', ' ', '|'],
            ['+', '-', '-', '+']
        ]


class Lavanderia(Ambiente):
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        super().__init__(portas, janelas)
        self.nome = 'lavanderia'
        self.h = 3
        self.w = 3
        self.forma = [
            ['+', '-', '-', '-', '+'],
            ['|', 'L', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', '|'],
            ['+', '-', '-', '-', '+']
        ]


class Quarto(Ambiente):
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        super().__init__(portas, janelas)
        self.nome = 'quarto'
        self.h = 4
        self.w = 4
        self.forma = [
            ['+', '-', '-', '-', '-', '+'],
            ['|', 'Q', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['+', '-', '-', '-', '-', '+']
        ]


class SalaDeJogos(Ambiente):
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        super().__init__(portas, janelas)
        self.nome = 'sala de jogos'
        self.h = 6
        self.w = 4
        self.forma = [
            ['+', '-', '-', '-', '-', '+'],
            ['|', 'S', 'J', 'O', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['+', '-', '-', '-', '-', '+']
        ]


class Cozinha(Ambiente):
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        super().__init__(portas, janelas)
        self.nome = 'cozinha'
        self.h = 3
        self.w = 5
        self.forma = [
            ['+', '-', '-', '-', '-', '-', '+'],
            ['|', 'C', 'O', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['+', '-', '-', '-', '-', '-', '+']
        ]


class SalaDeJantar(Ambiente):
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        super().__init__(portas, janelas)
        self.nome = 'sala de jantar'
        self.h = 5
        self.w = 4
        self.forma = [
            ['+', '-', '-', '-', '-', '+'],
            ['|', 'S', 'J', 'A', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', '|'],
            ['+', '-', '-', '-', '-', '+']
        ]


class SalaDeEstar(Ambiente):
    def __init__(self, portas=(0, 0, 0, 0), janelas=(0, 0, 0, 0)):
        super().__init__(portas, janelas)
        self.nome = 'sala de estar'
        self.h = 8
        self.w = 5
        self.forma = [
            ['+', '-', '-', '-', '-', '-', '+'],
            ['|', 'S', 'E', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', '|'],
            ['+', '-', '-', '-', '-', '-', '+']
        ]


ambientes = [
    Banheiro,
    Closet,
    Lavanderia,
    Quarto,
    SalaDeJogos,
    Cozinha,
    SalaDeJantar,
    SalaDeEstar
]

casa_ideal = [
    Closet([0, 0, 0, 1], [0, 0, 0, 0]),
    Banheiro([0, 0, 0, 1], [0, 0, 1, 0]),
    Banheiro([0, 0, 0, 1], [0, 0, 1, 0]),
    Closet([0, 0, 0, 1], [0, 0, 0, 0]),
    Lavanderia([0, 0, 0, 1], [0, 1, 1, 0]),
    Quarto([0, 0, 2, 1], [1, 0, 0, 0]),
    Quarto([0, 0, 2, 1], [0, 1, 0, 0]),
    Lavanderia([0, 0, 1, 1], [0, 1, 0, 0]),
    SalaDeEstar([1, 1, 2, 2], [1, 0, 0, 0]),
    Cozinha([1, 1, 1, 1], [0, 1, 0, 0]),
    SalaDeJogos([0, 1, 1, 0], [1, 0, 0, 1]),
    SalaDeJantar([1, 0, 2, 0], [0, 1, 0, 1])
]

qtd_ideal_ambientes = {
    'closet':         2,
    'banheiro':       2,
    'lavanderia':     2,
    'quarto':         2,
    'sala de estar':  1,
    'cozinha':        1,
    'sala de jantar': 1,
    'sala de jogos':  1
}

