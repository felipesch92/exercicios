class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor
        self.mostra_cor()

    def mostra_cor(self):
        print(f'A cor da bola é {self.cor}')

    def mostra_bola(self):
        print(f'A cor da bola é {self.cor}')
        print(f'A circunferência é {self.circunferencia}')
        print(f'O material é {self.material}')


bola_campo = Bola('azul', '55', 'couro')

bola_campo.mostra_bola()
bola_campo.troca_cor('vermelha')
bola_campo.mostra_bola()
