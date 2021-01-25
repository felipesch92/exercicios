# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        if self.idade < 21:
            if (self.idade + anos) > 20:
                crescer = (20 - self.idade) * 0.5
            else:
                crescer = anos * 0.5
            self.altura += crescer
        self.idade += anos

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self, tamanho):
        self.altura += tamanho

    def mostrar(self):
        print(f'Seja bem vindo {self.nome}, vamos analisar: ')
        print(f'Sua idade é de {self.idade} anos.')
        print(f'Seu peso é de {self.peso} kilos.')
        print(f'Sua altura é de {self.altura}!')


cliente1 = Pessoa('Felipe', 14, 79.5, 176.4)
cliente1.mostrar()
cliente1.envelhecer(14)
cliente1.emagrecer(5.4)
cliente1.crescer(5)
cliente1.mostrar()
