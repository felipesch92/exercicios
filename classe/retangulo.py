class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def mudar_comprimento(self, comprimento):
        self.comprimento = comprimento

    def mudar_largura(self, largura):
        self.largura = largura

    def mostrar_lados(self):
        return self.comprimento, self.largura

    def calcular_area(self):
        return self.comprimento * self.largura

    def calcular_perimetro(self):
        return (self.comprimento + self.largura) * 2

    def calcular_materiais(self):
        c = self.comprimento
        l = self.largura
        print(f'Para uma área de {c} de comprimento x {l} de largura:')
        print(f'Será necessário {self.calcular_perimetro()} metros de rodapé.')
        print(f'Será necessário {self.calcular_area()} metros de piso.')


sala = Retangulo(8, 5)
sala.calcular_materiais()
sala.mudar_largura(7)
sala.calcular_materiais()
sala.mudar_comprimento(10)
sala.calcular_materiais()
