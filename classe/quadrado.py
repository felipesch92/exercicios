class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def mudar_valor(self, tamanho):
        self.tamanho = tamanho

    def mostrar_lado(self):
        return self.tamanho

    def calcular_area(self):
        print(f'A área do quadrado é de {self.tamanho * 2}')


novo_quadrado = Quadrado(3)
print(novo_quadrado.mostrar_lado())
novo_quadrado.calcular_area()
novo_quadrado.mudar_valor(5)
novo_quadrado.calcular_area()
