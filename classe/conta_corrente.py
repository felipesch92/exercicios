# Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes
# atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque;
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente:
    def __init__(self, conta, cliente, saldo=0):
        self.conta = conta
        self.cliente = cliente
        self.saldo = saldo
        self.log = []

    def alterar_nome(self, nome):
        self.cliente = nome

    def depositar(self, valor):
        if not self.log:
            self.log.append(f'Saldo anterior R$ {self.saldo}')
        self.saldo += valor
        self.log.append(f'R$ +{valor}')

    def sacar(self, valor):
        if (self.saldo - valor) < 0:
            print('Não foi possível sacar, sua conta está zerada!')
        else:
            if not self.log:
                self.log.append(f'Saldo anterior R$ {self.saldo}')
            self.saldo -= valor
            self.log.append(f'R$ -{valor}')

    def extrato(self):
        print('-' * 40)
        print(f'Extrato da conta n {self.conta} - {self.cliente}')
        if self.log:
            for l in self.log:
                print(l)
        print(f'Saldo R$ {self.saldo}')
        print('-' * 40)

    def transferir(self, recebedor, valor):
        if (self.saldo - valor) < 0:
            print('Saldo insuficiente para realizar a transferência.')
        else:
            self.saldo -= valor
            recebedor.saldo += valor
            self.log.append(f'Transferẽncia conta {recebedor.conta} R$ -{valor}')
            recebedor.log.append(f'Transferência conta {self.conta} R$ +{valor}')


conta1 = ContaCorrente(299103, 'Felipe Schmaedecke', 5500)
conta2 = ContaCorrente(493212, 'Tamara Cardoso Gruetzmann', 6600)
conta2.transferir(conta1, 500)
conta2.depositar(1000)
conta1.extrato()
conta2.extrato()
