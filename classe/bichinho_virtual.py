'''Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
a. Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome,
Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso
tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então
não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer
momento.'''


class TAMAGUSHI:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 0
        self.saude = 100
        self.idade = 0

    def mudar_nome(self, nome):
        self.nome = nome

    def mudar_fome(self, fome):
        if -1 < fome < 101:
            self.fome = fome
        else:
            print('Informe um valor entre 0 e 100!')

    def mudar_saude(self, saude):
        if -1 < saude < 101:
            self.saude = saude
        else:
            print('Informe um valor entre 0 e 100!')

    def mudar_idade(self, idade):
        self.idade = idade

    def alimentar(self, q):
        if self.fome - q < 0:
            self.fome = 0
        else:
            self.fome -= q

    def brincar(self):
        if self.saude >= 90:
            self.saude = 100
        else:
            self.saude += 10

    def mostrar(self):
        print('-' * 40)
        print(f'Tamagushi {self.nome}')
        print(f'Fome: {self.fome}')
        print(f'Saúde: {self.saude}')
        print(f'Idade: {self.idade}')
        if self.saude > 80 and self.fome < 20:
            print('Seu humor está ótimo!')
        elif self.saude > 50 and self.fome < 40:
            print('Está de bom humor!')
        elif self.fome == 100:
            print(f'RIP {self.nome} Morreu de fome!')
        elif self.saude == 0:
            print(f'RIP {self.nome} Morreu de doença!')
        else:
            print('Está de mal humor!')
        print('-' * 40)


def alimentar_todos(lista, valor):
    for bicho in lista:
        bicho.alimentar(valor)

def brincar_todos(lista):
    for bicho in lista:
        bicho.brincar()

lista_bichinho = []
lista_bichinho.append(TAMAGUSHI('Scooby'))
lista_bichinho.append(TAMAGUSHI('Malvo'))
lista_bichinho.append(TAMAGUSHI('Mel'))
lista_bichinho.append(TAMAGUSHI('Thor'))

for bicho in lista_bichinho:
    bicho.mudar_saude(20)
    bicho.mudar_fome(70)

brincar_todos(lista_bichinho)
alimentar_todos(lista_bichinho, 20)
for b in lista_bichinho:
    b.mostrar()
