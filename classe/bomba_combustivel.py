'''Faça um programa completo utilizando classes e métodos que:
a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
i. tipoCombustivel.
ii. valorLitro
iii. quantidadeCombustivel
b. Possua no mínimo esses métodos:
i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros
que foi colocada no veículo
ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser
pago pelo cliente.
iii. alterarValor( ) – altera o valor do litro do combustível.
iv. alterarCombustivel( ) – altera o tipo do combustível.
v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.'''


class BombaCombustivel():
    def __init__(self, tipo, valor, litros):
        self.tipo = tipo
        self.valor = valor
        self.litros = litros

    def abastecer_por_valor(self, valor):
        self.altera_quantidade_combustivel(self.litros - (valor / self.valor))

    def abastecer_por_litro(self, qtd):
        self.altera_quantidade_combustivel(self.litros - qtd)

    def alterar_valor(self, valor):
        self.valor = valor

    def alterar_combustivel(self, tipo):
        self.tipo = tipo

    def altera_quantidade_combustivel(self, qtd):
        self.litros = qtd

    def status(self):
        print('-' * 40)
        print(f'Combustivel: {self.tipo}')
        print(f'Valor: {self.valor}')
        print(f'Litros: {self.litros:.2f}')
        print('-' * 40)


b1 = BombaCombustivel('Gasolina', 3, 5000)
b1.abastecer_por_valor(30)
b1.abastecer_por_litro(50)
b1.alterar_combustivel('Diesel')
b1.alterar_valor(3.69)
b1.abastecer_por_valor(224)
b1.status()
