'''Faça uma classe contaInvestimento que seja semelhante a classe contaBancaria, com
a diferença de que se adicione um atributo taxaJuros. Forneça um construtor que configure tanto o saldo inicial como a
taxa de juros. Forneça um método adicioneJuros (sem parâmetro explícito) que adicione juros à conta. Escreva um
programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o
método adicioneJuros() cinco vezes e imprime o saldo resultante.'''


class ContaInvestimento():
    def __init__(self, conta, titular, valor):
        self.conta = conta
        self.titular = titular
        self.valor = valor
        self.tx_juros = 0.01

    def adicionar_juros(self):
        self.valor += self.valor * self.tx_juros

    def alterar_taxa(self, tx):
        self.tx_juros = tx / 100

    def extrato(self):
        print('-' * 40)
        print(f'Conta: {self.conta}')
        print(f'Titular: {self.titular}')
        print(f'Valor R$: {self.valor:.2f}')
        print('-' * 40)


c1 = ContaInvestimento(3092, 'Felipe Schmaedecke', 3000)
#c1.alterar_taxa(2.5)
c1.adicionar_juros()
c1.adicionar_juros()
c1.adicionar_juros()
c1.adicionar_juros()
c1.adicionar_juros()
c1.extrato()
