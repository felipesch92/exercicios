'''Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os
métodos comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos,
alimentando-os com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição.
Experimente fazer com que um macaco coma o outro. É possível criar um macaco canibal?'''
from time import sleep


class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def ver_bucho(self):
        if self.bucho:
            print('Bucho:')
            for a in self.bucho:
                if 'Macaco' in str(type(a)):
                    print(f'Você comeu um Macaco chamado {a.nome}!')
                else:
                    print(a)
        else:
            print(f'O macaco {self.nome} está com o bucho vazio!')

    def digerir(self):
        if self.bucho:
            for a in self.bucho:
                if 'Macaco' in str(type(a)):
                    print(f'Digerindo um Macaco chamado {a.nome}!')
                    sleep(1)
                    print('Esse é mais demorado....')
                    sleep(3)
                else:
                    print(f'Evacuando {a}...')
                sleep(1)
        print(f'O macaco {self.nome} está com o bucho vazio!')


m1 = Macaco('Malvo')
m1.comer('Maça')
m1.comer('Banana')
m1.comer('Pão')
m1.comer('Ração')
#m1.ver_bucho()
#m1.digerir()

m2 = Macaco('Scooby')
m2.comer('Banana')
m2.comer('Maça')
m2.comer(m1)
m2.comer('Carne')
m2.comer('Massa')
#m2.ver_bucho()
m2.digerir()
