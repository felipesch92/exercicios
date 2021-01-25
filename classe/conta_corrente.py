# Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes
# atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque;
# No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente:
    log = []
    def __init__(self, conta, cliente, saldo=0):
        self.conta = conta
        self.cliente = cliente
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.cliente = nome

    def depositar(self, valor):
        if not ContaCorrente.log:
            ContaCorrente.log.append(f'Saldo anterior R$ {self.saldo}')
        self.saldo += valor
        ContaCorrente.log.append(f'R$ +{valor}')

    def sacar(self, valor):
        if (self.saldo - valor) < 0:
            print('Não foi possível sacar, sua conta está zerada!')
        else:
            if not ContaCorrente.log:
                ContaCorrente.log.append(f'Saldo anterior R$ {self.saldo}')
            self.saldo -= valor
            ContaCorrente.log.append(f'R$ -{valor}')

    def extrato(self):
        print('-' * 40)
        print(f'Extrato da conta n {self.conta}')
        print(f'Cliente {self.cliente}')
        if ContaCorrente.log:
            for l in ContaCorrente.log:
                print(l)
        print(f'Saldo R$ {self.saldo}')
        print('-' * 40)


conta1 = ContaCorrente(299103, 'Felipe Schmaedecke', 5500)
conta1.extrato()
conta1.sacar(4000)
conta1.depositar(1500)
conta1.extrato()
conta1.sacar(350)
conta1.depositar(3500.68)
conta1.extrato()
